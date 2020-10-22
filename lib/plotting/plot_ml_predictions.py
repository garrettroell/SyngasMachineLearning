import matplotlib.pyplot as plt

def plot_ml_predictions(ml_dict, type, title, save_fig):
    filename = 'images/' + title.replace(' ', '_') + '.png'
    print(filename)

    _, _ = plt.subplots(3,3,figsize=(17,17))
    plt.suptitle(title, fontsize=20)
 
    compositions = range (1,8)
    for comp in compositions:
        plt.subplot(3, 3, comp)

        comp_data=ml_dict[f'composition_{comp}']
        frame = '33'+str(comp)
        plt.subplot(frame)

        title = f'Comp {comp}, test rmse={comp_data["test_rmse"].round(2)}, test r2={comp_data["test_r2"].round(3)}'
        plt.title(title,fontsize=15)
        plt.xlabel(f'measured {type}', fontsize = 12)
        plt.ylabel(f'predicted {type}', fontsize = 12)
        plt.scatter(comp_data[f'train_measured_{type}s'], comp_data[f'train_predicted_{type}s'], color='b')
        plt.scatter(comp_data[f'test_measured_{type}s'], comp_data[f'test_predicted_{type}s'], color='r')

    if save_fig:
        plt.savefig(filename, dpi=150)