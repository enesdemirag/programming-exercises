from matplotlib import pyplot as plt
from matplotlib import animation


class Visualizer(object):
    def __init__(self, callback=None, interval=100.0, simulation_time=20.0, initial=(0, 0, 0, 0, 0, 0)):
        # Set loop interval
        self.interval = interval
        self.simulation_time = simulation_time
        # Create figure
        self.fig = plt.figure(1, figsize=(13, 6), dpi=80)
        # Create animation plot area
        self.animation_plot = self.fig.add_subplot(223)
        # Create position plot
        self.position_plot = self.fig.add_subplot(221)
        self.position_plot.set_xlim((0, self.simulation_time))
        self.position_plot.set_ylim((-20, 20))
        self.position_plot_patch = GraphPlot()
        self.position_plot.add_patch(self.position_plot_patch.first_patch)
        self.position_plot.add_patch(self.position_plot_patch.second_patch)
        self.position_plot.text(0.85, 0.8, 'Red:  x\nBlue: y', transform=self.position_plot.transAxes)
        self.position_plot.text(0.03, 0.9, 'Position Plot', transform=self.position_plot.transAxes)
        # Create velocity plot
        self.velocity_plot = self.fig.add_subplot(222)
        self.velocity_plot.set_xlim((0, self.simulation_time))
        self.velocity_plot.set_ylim((-20, 20))
        self.velocity_plot_patch = GraphPlot()
        self.velocity_plot.add_patch(self.velocity_plot_patch.first_patch)
        self.velocity_plot.add_patch(self.velocity_plot_patch.second_patch)
        self.velocity_plot.text(0.83, 0.8, 'Red:  Vx\nBlue: Vy', transform=self.velocity_plot.transAxes)
        self.velocity_plot.text(0.03, 0.9, 'Velocity Plot', transform=self.velocity_plot.transAxes)
        # Create acceleration plot
        self.acceleration_plot = self.fig.add_subplot(224)
        self.acceleration_plot.set_xlim((0, self.simulation_time))
        self.acceleration_plot.set_ylim((-30, 30))
        self.acceleration_plot_patch = GraphPlot()
        self.acceleration_plot.add_patch(self.acceleration_plot_patch.first_patch)
        self.acceleration_plot.add_patch(self.acceleration_plot_patch.second_patch)
        self.acceleration_plot.text(0.83, 0.8, 'Red:  Ax\nBlue: Ay', transform=self.acceleration_plot.transAxes)
        self.acceleration_plot.text(0.03, 0.9, 'Acceleration Plot', transform=self.acceleration_plot.transAxes)
        # Create dynamic label for simulation time
        self.sim_time_label = self.animation_plot.text(0.03, 0.9, '', transform=self.animation_plot.transAxes)
        # Set axes limit
        self.animation_plot.set_xlim((-20, 20))
        self.animation_plot.set_ylim((0, 30))
        # Create the mass object
        self.patch = plt.Rectangle((0, 0), width=10, height=5, fc='b')
        # Add the patches
        self.animation_plot.add_patch(self.patch)
        # Create animation core
        self.animate = animation.FuncAnimation(self.fig, self.animate, interval=self.interval,
                                               blit=True, repeat=True, init_func=self.init_func)
        # Set initials to zero
        self.sim_time = 0
        self.x = initial[0]
        self.y = initial[1]
        self.vx = initial[2]
        self.vy = initial[3]
        self.ax = initial[4]
        self.ay = initial[5]
        # Set callback
        self.cb_func = callback
        plt.show()

    def init_func(self):
        # Set initials to zero
        self.sim_time_label.set_text("")
        self.patch.xy = (0, 0)

        pos_plot = self.position_plot_patch.init_func()
        vel_plot = self.velocity_plot_patch.init_func()
        acc_plot = self.acceleration_plot_patch.init_func()
        ret_ = [self.patch, self.sim_time_label] + acc_plot + vel_plot + pos_plot
        # return the objects to be redrawn
        return ret_

    def animate(self, i):
        # update simulation time, i = n'th time that the method has
        # called, thus each represents self.interval ms of delay.
        self.sim_time = float(i) / (1000.0 / self.interval)

        # Update time
        self.sim_time_label.set_text("Simulation Time: " + str(self.sim_time))

        # Get object xy from callback
        (x, y) = self.cb_func(self.sim_time)
        # Set the position of object
        vx = (x - self.x) / (self.interval / 1000.0)
        vy = (y - self.y) / (self.interval / 1000.0)

        self.ax = (vx - self.vx) / (self.interval / 1000.0)
        self.ay = (vy - self.vy) / (self.interval / 1000.0)
        self.vx = vx
        self.vy = vy
        self.x = x
        self.y = y
        self.patch.xy = (x - 5, y - 2.5)

        pos_plot = self.position_plot_patch.update([[self.sim_time, x], [self.sim_time, y]])
        vel_plot = self.velocity_plot_patch.update([[self.sim_time, vx], [self.sim_time, vy]])
        acc_plot = self.acceleration_plot_patch.update([[self.sim_time, self.ax], [self.sim_time, self.ay]])
        ret_ = [self.patch, self.sim_time_label] + acc_plot + vel_plot + pos_plot
        # return the objects to be redrawn
        return ret_


class GraphPlot():
    def __init__(self):
        self.first_patch = plt.Polygon([[0, 0]], closed=None, fill=None, edgecolor='r')
        self.second_patch = plt.Polygon([[0, 0]], closed=None, fill=None, edgecolor='b')

    def init_func(self):
        self.first_patch.xy = [[0, 0]]
        self.second_patch.xy = [[0, 0]]
        return [self.first_patch, self.second_patch]

    def update(self, data):
        # Add current x position to x graph
        arr = self.first_patch.get_xy().tolist()
        arr.append(data[0])
        self.first_patch.xy = arr

        # Add current y position to y graph
        arr = self.second_patch.get_xy().tolist()
        arr.append(data[1])
        self.second_patch.xy = arr

        return [self.first_patch, self.second_patch]
