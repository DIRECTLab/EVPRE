# Model Information
## FASTSim Model
The FASTSim model utilizes the FASTSim energy algorithm to calculate node edge power cost. It does this by creating a small simulation (cycle in FASTSim terminology), and within that simulation creating a small slice emulating the edge's length (i.e., road section length) and one way height differential.

### FASTSim Vehicle Model
The Ford Focus Electric FASTSim vehicle model was designed by utilizing the [FASTSim Excel version](https://www.nrel.gov/transportation/fastsim.html).

Sample vehicles are also available through the [FASTSim Python version](https://www.nrel.gov/transportation/fastsim.html).

Steps to create a vehicle model:
1. Download the Excel version of FASTSim and load a comparable vehicle.
2. Modify the vehicle parameters to meet your vehicle's parameters.
3. Grab the new vehicle's data and append it to the FASTSim vehicle model CSV.
4. Modify the index in config.py to match your vehicle.

## Simple Energy and Vehicle Model
The simple energy model utilizes calculations based on [Power-based electric vehicle energy consumption model: Model development and validation](https://www.sciencedirect.com/science/article/pii/S030626191630085X). The energy model relies on the user to implement the proper vehicle parameters into the config.py file.

The simple energy model calculates instantaneous power from the following parameters:
- Velocity
- Mass
- Acceleration
- Rolling resistance
- Air resistance
- Gravity (incline)

## Installation 
To install fastsim: Navigate to the directory (example: fastsim-2021a) that contains the fastsim source code. Run pip install . to install it to your pip.
