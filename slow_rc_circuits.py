import math
import statistics as stat
import matplotlib.pyplot as plt
from error_calc import Rules

def slope(x:list, y:list):
	x_avg = sum(x) / len(x)
	y_avg = sum(y) / len(y)

	return y_avg / x_avg

def tau_uncertainty(tau:list):
	return stat.pstdev(tau) / math.sqrt(len(tau))

if __name__ == '__main__':
	print()

	#Experiment 1:
	print('EXPERIMENT 1:')
	time = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120] #s
	V_charge = [0, 4.31, 6.9, 8.54, 9.63, 10.26, 10.67, 10.93, 11.1, 11.21, 11.28, 11.32, 11.35] #V
	V_discharge = [12, 7.64, 4.77, 3.06, 1.93, 1.23, 0.86, 0.52, 0.34, 0.22, 0.15, 0.1, 0.07] #V

	print(f'Charge Slope: {round(slope(V_charge, time), 2)}')
	print(f'Discharge Slope: -{round(slope(V_discharge, time), 2)}')

	plt.plot(time, V_charge)
	plt.show()
	plt.plot(time, V_discharge)
	plt.show()

	print()

	#Experiment 2:
	print('EXPERIMENT 2:')
	V_0 = 12.0 #V
	V_c = (0.632)*V_0 #V
	V_d = (0.368)*V_0 #V

	print(f'V_c = {V_c}')
	print(f'V_d = {V_d}')

	t_charge = [21.51, 21.01, 21.32, 21.52, 20.88, 21.54, 21.52, 21.74, 20.83, 21.57] #s
	t_discharge = [23.51, 23.58, 23.63, 23.63, 23.35, 23.48, 23.28, 23.36, 22.93, 23.45] #s

	tau_charge = sum(t_charge) / len(t_charge)
	tau_discharge = sum(t_discharge) / len(t_discharge)

	print(f'τ_c = {round(tau_charge, 2)}')
	print(f'τ_d = {round(tau_discharge, 2)}')

	uncertainty_tau_charge = tau_uncertainty(t_charge)
	uncertainty_tau_discharge = tau_uncertainty(t_discharge)

	print(f'δτ_c = {round(uncertainty_tau_charge, 2)}')
	print(f'δτ_d = {round(uncertainty_tau_discharge, 2)}')

	print()

	#Experiment 3:
	print('EXPERIMENT 3:')
	R = 501.3 * 1000 #ohm
	C = 43.8 * 10e-7 #F

	print(f'R = {round(R, 2)}')
	print(f'C = {round(C, 7)}')

	tau = (R)*(C)

	u_x = 0.1 / (2 * math.sqrt(3))
	uncertainty_tau = Rules.rule4([R, C], [u_x * 1000, u_x * 10**-6], [1, 1], tau)

	print(f'τ = {round(tau, 2)}')
	print(f'δτ = {round(uncertainty_tau, 2)}')
	

	print()
