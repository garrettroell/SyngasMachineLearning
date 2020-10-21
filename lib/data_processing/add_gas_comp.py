from initial_value_problem.get_gas_comp import get_gas_comp

def add_gas_comp(input_data):

    CO, CO2, H2, flow_rate = [], [], [], []

    for index, _ in input_data.iterrows():
        comp = index[0]
        gas_comp = get_gas_comp()[comp]
        CO.append(gas_comp[0])
        CO2.append(gas_comp[1])
        H2.append(gas_comp[2])
        flow_rate.append(gas_comp[3])
        

    output_data = input_data.copy()
    output_data['CO'] = CO
    output_data['CO2'] = CO2
    output_data['H2'] = H2
    output_data['Flow Rate'] = flow_rate
    
    return output_data