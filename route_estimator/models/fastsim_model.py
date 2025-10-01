import numpy as np
import os
import pathlib
import fastsim as fs

class fastsim_energy_model:
    def __init__(self, fastsim_vehicle_yaml: str):
        self.fastsim_vehicle_yaml = fastsim_vehicle_yaml
    
    def get_consumed_kwh_fastsim(self, avg_speed_mps: float, grade: float, distance_m: float, idle_seconds: int = 0) -> float:
        # FASTSim likes a gentle increase, so we will build a ramp in speed that will be removed from the final equation
        cyc_mps_builder = []
        cur_speed = 0
        while cur_speed < avg_speed_mps:
            cyc_mps_builder.append(cur_speed)
            cur_speed = min(avg_speed_mps, cur_speed + 1.0)

        # Add an extra 10 seconds to stabilize calculation (not sure if necessary)
        for x in range(10):
            cyc_mps_builder.append(cur_speed)

        # The index to start calculating power usage
        # start_index = len(cyc_mps_builder)

        distance_traveled = avg_speed_mps
        cyc_mps_builder.append(avg_speed_mps)

        # Create a constant velocity array in meters/sec until we've covered all the distance
        # NOTE: This will overestimate by a distance of 0 - avg_speed_mps.
        while(distance_traveled < distance_m):
            distance_traveled += avg_speed_mps
            cyc_mps_builder.append(avg_speed_mps)

        # stop_index = len(cyc_mps_builder)

        while cur_speed > 0:
            cyc_mps_builder.append(cur_speed)
            cur_speed = max(0, cur_speed - 1.0)

        # Add an extra 10 seconds to stabilize calculation (not sure if necessary)
        for x in range(10):
            cyc_mps_builder.append(cur_speed)

        # Create a FASTSim cycle from the data
        cyc_mps = np.array(cyc_mps_builder)
        cyc_secs = np.array([x for x in range(len(cyc_mps))])
        cyc_grade = np.array([grade for x in range(len(cyc_mps))])
        cycle_dict = {
            'time_seconds': np.array(cyc_secs).tolist(),
            'speed_mps': np.array(cyc_mps).tolist(),
            'grade': np.array(cyc_grade).tolist()
        }
        cyc = fs.Cycle.from_pydict(cycle_dict)

        # Create a FASTSim vehicle from the YAML file
        veh = fs.Vehicle.from_file(self.fastsim_vehicle_yaml)

        sim = fs.SimDrive(veh, cyc)
        sim.walk()
        sim_power_kwh = sim.essCurKwh[0] - sim.essCurKwh[-1]
        
        print(f'Sim calculated kWh loss: {sim_power_kwh}')

        if idle_seconds > 0:
            sim_power_kwh += (veh.auxKw * idle_seconds) / 3600

        return sim_power_kwh
        



if __name__ == "__main__":
    for vehicle_yaml in ["vehicles/2016 CHEVROLET Spark EV.yaml",
                         "vehicles/2016 Leaf 24 kWh.yaml",
                         "vehicles/2018 Nissan Leaf 40 kWh.yaml",
                         "vehicles/kenworth_t680e.yaml"] : 
        model = fastsim_energy_model(vehicle_yaml)
        print(f"{vehicle_yaml} - no idle: {model.get_consumed_kwh_fastsim(15, 0.1, 100.0)} kWh")
        print(f"{vehicle_yaml} - 3600s idle: {model.get_consumed_kwh_fastsim(15, 0.1, 100.0, 3600)} kWh")
