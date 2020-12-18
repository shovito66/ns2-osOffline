from functions import *
import matplotlib.pyplot as plt

# received_packets = 0
# sent_packets = 0
# dropped_packets = 0
# total_delay = 0
# received_bytes = 0

# start_time = 1000000
# end_time = 0

# header_bytes = 20  # constants
# sent_time = {}  # Empty Dictionary

# test_str = "GFG is for Geeks"
# N = 3
# # Get Nth word in String
# # using split()
# res = test_str.split()
# print(res[3])


Y_output_flow = {
    'throughput': [],
    'avgDelay': [],
    'deliveryRatio': [],
    'dropRatio': [],
}
Y_output_node = {
    'throughput': [],
    'avgDelay': [],
    'deliveryRatio': [],
    'dropRatio': [],
}
Y_output_area = {
    'throughput': [],
    'avgDelay': [],
    'deliveryRatio': [],
    'dropRatio': [],
}

X_input = {}
X_input['flow'] = [10, 20, 30, 40, 50]
X_input['node'] = [20, 40, 60, 80, 100]
X_input['area'] = [250, 500, 750, 1000, 1250]

fileNames = ['500_40_10.tr', '500_40_20.tr', '500_40_30.tr',
             '500_40_40.tr', '500_40_50.tr']  # flow Varying

fileNames1 = ['500_20_20.tr', '500_40_20.tr', '500_60_20.tr',
              '500_80_20.tr', '500_100_20.tr']  # node Varying

fileNames2 = ['250_40_20.tr', '500_40_20.tr', '750_40_20.tr',
              '1000_40_20.tr', '1250_40_20.tr']  # area Varying

# Opening file
i = 0
for name in fileNames:

    temp_List = {}
    print("Flow Variation File{}    :{}".format(i+1, name))
    file = open('FlowVariation/'+name, 'r')
    # Y_output_flow[i] = myFunctionFlow(file, 0)
    # Y_output['flow']['throughput'][i] = Y_output_flow[i]['throughput']
    # Y_output['flow']['avgDelay'][i] = Y_output_flow[i]['avgDelay']
    # Y_output['flow']['deliveryRatio'][i] = Y_output_flow[i]['deliveryRatio']
    # Y_output['flow']['dropRatio'][i] = Y_output_flow[i]['dropRatio']
    temp_List = myFunctionFlow(file, 0)
    Y_output_flow['throughput'].append(temp_List['throughput'])
    Y_output_flow['avgDelay'].append(temp_List['avgDelay'])
    Y_output_flow['deliveryRatio'].append(temp_List['deliveryRatio'])
    Y_output_flow['dropRatio'].append(temp_List['dropRatio'])

    print("-------------------------------------\n")
    ++i

temp_List.clear()
i = 0
for name in fileNames1:

    temp_List = {}
    print("Node Variation File{}    :{}".format(i+1, name))
    file = open('NodeVariation/'+name, 'r')
    # Y_output_flow[i] = myFunctionFlow(file, 0)
    # Y_output['flow']['throughput'][i] = Y_output_flow[i]['throughput']
    # Y_output['flow']['avgDelay'][i] = Y_output_flow[i]['avgDelay']
    # Y_output['flow']['deliveryRatio'][i] = Y_output_flow[i]['deliveryRatio']
    # Y_output['flow']['dropRatio'][i] = Y_output_flow[i]['dropRatio']
    temp_List = myFunctionFlow(file, 0)
    Y_output_node['throughput'].append(temp_List['throughput'])
    Y_output_node['avgDelay'].append(temp_List['avgDelay'])
    Y_output_node['deliveryRatio'].append(temp_List['deliveryRatio'])
    Y_output_node['dropRatio'].append(temp_List['dropRatio'])

    print("-------------------------------------\n")
    ++i

temp_List.clear()
i = 0
for name in fileNames2:

    temp_List = {}
    print("Node Variation File{}    :{}".format(i+1, name))
    file = open('AreaVariation/'+name, 'r')
    # Y_output_flow[i] = myFunctionFlow(file, 0)
    # Y_output['flow']['throughput'][i] = Y_output_flow[i]['throughput']
    # Y_output['flow']['avgDelay'][i] = Y_output_flow[i]['avgDelay']
    # Y_output['flow']['deliveryRatio'][i] = Y_output_flow[i]['deliveryRatio']
    # Y_output['flow']['dropRatio'][i] = Y_output_flow[i]['dropRatio']
    temp_List = myFunctionFlow(file, 0)
    Y_output_area['throughput'].append(temp_List['throughput'])
    Y_output_area['avgDelay'].append(temp_List['avgDelay'])
    Y_output_area['deliveryRatio'].append(temp_List['deliveryRatio'])
    Y_output_area['dropRatio'].append(temp_List['dropRatio'])

    print("-------------------------------------\n")
    ++i


y_Attributes=['throughput','avgDelay','deliveryRatio','dropRatio']
for y_attribute in y_Attributes:
    plotGraph(X_input['flow'], Y_output_flow[y_attribute],
          'Flow', y_attribute, 'Flow Variation: {} Vs Flow'.format(y_attribute))

for y_attribute in y_Attributes:
    plotGraph(X_input['node'], Y_output_node[y_attribute],
          'Node', y_attribute, 'Node Variation: {} Vs Node'.format(y_attribute))

for y_attribute in y_Attributes:
    plotGraph(X_input['area'], Y_output_area[y_attribute],
          'Area', y_attribute, 'Area Variation: {} Vs Area'.format(y_attribute))

# plotGraph(X_input['flow'], Y_output_flow,
#           'Flow',y_Attributes,'Flow Variation:')


# print(Y_output_flow[0])















# for line in file:
#     # print(line)
#     count = 1
#     words = line.split()
#     event = words[0]
#     time_sec = float(words[1])
#     node = int(words[2].replace('_', ''))
#     layer = words[3]
#     packet_id = int(words[5])
#     packet_type = words[6]
#     packet_bytes = int(words[7])
#     # print(node)
#     # set start time for the first line
#     if start_time > time_sec:
#         start_time = time_sec

#     if layer == "AGT" and packet_type == "tcp":

#         if event == "s":
#             sent_time[packet_id] = time_sec
#             sent_packets += 1

#         elif event == "r":
#             delay = time_sec - sent_time[packet_id]

#             total_delay += delay

#             bytes = (packet_bytes - header_bytes)
#             received_bytes += bytes

#             received_packets += 1

#     if packet_type == "tcp" and event == "D":
#         dropped_packets += 1

# end_time = time_sec
# simulation_time = end_time - start_time

# print("Sent Packets     :{}".format(sent_packets))
# print("Dropped Packets  :{}".format(dropped_packets))
# print("Received Packets :{}".format(received_packets))
# print("-------------------------------------------------------------")
# print("Throughput       :{} bits/sec".format(((received_bytes * 8) / simulation_time)))
# print("Average Delay    :{} seconds".format((total_delay / received_packets)))
# print("Delivery ratio   :{} ".format((received_packets / sent_packets)))
# print("Drop ratio       :{} ".format((dropped_packets / sent_packets)))

# event = words[0]
# time_sec = float(words[1])
# node = words[2].replace('_', '')
# layer = words[3]
# packet_id = words[5]
# packet_type = words[6]
# packet_bytes = int(words[7])
# # print(node)
# # set start time for the first line
# if start_time > time_sec:
#     start_time = time_sec

# if layer == "AGT" and packet_type == "tcp":

#     if event == "s":
#         sent_time[packet_id] = time_sec
#         sent_packets += 1

#     elif event == "r":
#         delay = time_sec - sent_time[packet_id]

#         total_delay += delay

#         bytes = (packet_bytes - header_bytes)
#         received_bytes += bytes

#         received_packets += 1

# if packet_type == "tcp" and event == "D":
#     dropped_packets += 1

# end_time = time_sec
# simulation_time = end_time - start_time

# print("Sent Packets     :{}".format(sent_packets))
# print("Dropped Packets  :{}".format(dropped_packets))
# print("Received Packets :{}".format(received_packets))

# print("-------------------------------------------------------------")
# print("Throughput       :{} bits/sec".format(((received_bytes * 8) / simulation_time)))
# print("Average Delay    :{} seconds".format((total_delay / received_packets)))
# print("Delivery ratio   :{} ".format((received_packets / sent_packets)))
# print("Drop ratio       :{} ".format((dropped_packets / sent_packets)))
