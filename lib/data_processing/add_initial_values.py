from initial_value_problem.get_initial_values import get_initial_values

def add_initial_values(input_data, smooth_data):

    acetate_0, biomass_0, butanol_0, butyrate_0, ethanol_0 = [], [], [], [], []

    for index, _ in input_data.iterrows():
        comp = index[0]
        smooth_comp_data = smooth_data.loc[comp]
        initial_values = get_initial_values(smooth_comp_data)
        acetate_0.append (initial_values[0])
        biomass_0.append (initial_values[1])
        butanol_0.append (initial_values[2])
        butyrate_0.append(initial_values[3])
        ethanol_0.append (initial_values[4])

    output_data = input_data.copy()
    output_data['acetate_0'] = acetate_0
    output_data['biomass_0'] = biomass_0
    output_data['butanol_0'] = butanol_0
    output_data['butyrate_0'] = butyrate_0
    output_data['ethanol_0'] = ethanol_0
    
    return output_data