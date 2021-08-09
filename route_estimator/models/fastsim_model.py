import numpy as np
import os
import pathlib
from fastsim import simdrive
from fastsim import vehicle
from fastsim import cycle

class fastsim_model:
    def __init__(self):
        pass

    def get_consumed_kwh_fastsim(self, fastsim_vehicle_model_csv_path: str, avg_speed_mps: float, grade: float, distance_m: float) -> float:
        # FASTSim likes a gentle increase, so we will build a ramp in speed that will be removed from the final equation
        cyc_mps_builder = []
        cur_speed = 0
        while cur_speed < avg_speed_mps:
            cyc_mps_builder.append(cur_speed)
            cur_speed = min(avg_speed_mps, cur_speed + 1.0)

        # Add an extra 10 seconds to stabilize calculation (not sure if necessary)
        for x in range(10):
            cyc_mps_builder.append(avg_speed_mps)

        # The index to start calculating power usage
        start_index = len(cyc_mps_builder)

        distance_traveled = avg_speed_mps
        cyc_mps_builder.append(avg_speed_mps)

        # Create a constant velocity array in meters/sec until we've covered all the distance
        # NOTE: This will overestimate by a distance of 0 - avg_speed_mps. 
        while(distance_traveled < distance_m):
            distance_traveled += avg_speed_mps
            cyc_mps_builder.append(avg_speed_mps)
        
        # Create a FASTSim cycle from the data
        cyc_mps = np.array( cyc_mps_builder)
        cyc_secs = np.array([x for x in range(len(cyc_mps))])
        cyc_grade = np.array([grade for x in range(len(cyc_mps))])

        # print(cyc_mps)
        # print(cyc_secs)
        # print(cyc_grade)

        cycle_dict = {
            'cycSecs': cyc_secs,
            'cycMps': cyc_mps,
            'cycGrade': cyc_grade
        }
        
        cyc = cycle.Cycle(cyc_dict=cycle_dict)
        cyc_jit = cyc.get_numba_cyc()
        
        veh = vehicle.Vehicle(1, fastsim_vehicle_model_csv_path)
        # veh.regenA = 50
        print(veh.Scenario_name)
        # print(veh.vehKg)
        veh_jit = veh.get_numba_veh()

        sim_drive = simdrive.SimDriveJit(cyc_jit, veh_jit)
        sim_drive.sim_drive(1) 
        sim_power_kwh = sim_drive.essCurKwh[start_index] - sim_drive.essCurKwh[-1]

        # print(f'Sim calculated kWh loss: {sim_power}')

        return sim_power_kwh


focus_csv = str(list(pathlib.Path(os.getcwd()).rglob('*fastsim_focus.csv'))[0])
fastsim_model().get_consumed_kwh_fastsim(focus_csv, 15, 0.1, 100.0)