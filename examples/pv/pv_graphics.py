import matplotlib.pyplot as plt
from pecos.graphics import plot_timeseries, plot_scatter

def graphics(filename, pm):
    
    # Plot DC Power over time
    plt.figure(figsize = (5.0,2.5))
    try:
        plotdata = pm.df[pm.trans['DC Power']]
    except:
        plotdata = None
    plot_timeseries(plotdata, pm.tfilter, yaxis_min=-200)
    plt.savefig(filename + '_custom1.jpg', format='jpg', dpi=1000)
    plt.close()  
    
    # Plot DC Power vs POA
    plt.figure(figsize = (5.0,2.5))
    try:
        plotdata_x = pm.df[pm.trans['POA']][pm.tfilter]
        plotdata_y = pm.df[pm.trans['DC Power']][pm.tfilter]
        if plotdata.isnull().all().all():
            plotdata_x = None
            plotdata_y = None
    except:
        plotdata_x = None
        plotdata_y = None
    plot_scatter(plotdata_x,plotdata_y, yaxis_min=-200)
    plt.xlabel('POA', fontsize=8)
    plt.ylabel('DC Power', fontsize=8)
    plt.savefig(filename + '_custom2.jpg', format='jpg', dpi=1000)
    plt.close()  
        
    # Plot Irradiance over time
    plt.figure(figsize = (5.0,2.5))
    try:
        irr_columns = pm.trans['GHI']
        irr_columns.extend(pm.trans['DHI'])
        irr_columns.extend(pm.trans['DNI'])
        plotdata = pm.df[irr_columns]
    except:
        plotdata = None
    plot_timeseries(plotdata, pm.tfilter, yaxis_min=-200, yaxis_max=1200)
    plt.legend(['GHI', 'DHI', 'DNI'], fontsize=8) 
    plt.ylabel('Irradiance', fontsize=8) 
    plt.savefig(filename +'_custom3.jpg', format='jpg', dpi=1000)
    plt.close()  
