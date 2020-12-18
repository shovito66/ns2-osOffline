import matplotlib.pyplot as plt

def myFunctionFlow(file,choice):
    Y_output = {}
    received_packets = 0
    sent_packets = 0
    dropped_packets = 0
    total_delay = 0
    received_bytes = 0

    start_time = 1000000
    end_time = 0

    header_bytes = 20  # constants
    sent_time = {}  # Empty Dictionary
    for line in file:
        count = 1
        words = line.split()
        event = words[0]
        time_sec = float(words[1])
        node = words[2].replace('_', '')
        layer = words[3]
        packet_id = words[5]
        packet_type = words[6]
        packet_bytes = int(words[7])
        # print(node)
        # set start time for the first line
        if start_time > time_sec:
            start_time = time_sec

        if layer == "AGT" and packet_type == "tcp":

            if event == "s":
                sent_time[packet_id] = time_sec
                sent_packets += 1

            elif event == "r":
                delay = time_sec - sent_time[packet_id]

                total_delay += delay

                bytes = (packet_bytes - header_bytes)
                received_bytes += bytes

                received_packets += 1

        if packet_type == "tcp" and event == "D":
            dropped_packets += 1

    end_time = time_sec
    simulation_time = end_time - start_time

    print("Sent Packets     :{}".format(sent_packets))
    print("Dropped Packets  :{}".format(dropped_packets))
    print("Received Packets :{}".format(received_packets))

    print("-------------------------------------------------------------")
    print("Throughput       :{} bits/sec".format(((received_bytes * 8) / simulation_time)))
    print("Average Delay    :{} seconds".format((total_delay / received_packets)))
    print("Delivery ratio   :{} ".format((received_packets / sent_packets)))
    print("Drop ratio       :{} ".format((dropped_packets / sent_packets)))

    #   flow varying
    #   Area: 500 Node:40
    # for i in range(5):
    #     # print(i)
    #     Y_output['flow']['throughput'][i] = (received_bytes * 8) / simulation_time
    #     Y_output['flow']['avgDelay'][i] = total_delay / received_packets
    #     Y_output['flow']['deliveryRatio'][i] = received_packets / sent_packets
    #     Y_output['flow']['dropRatio'][i] = dropped_packets / sent_packets

        # print(i)
    if choice==0:
        Y_output['throughput'] = (received_bytes * 8) / simulation_time
        Y_output['avgDelay'] = total_delay / received_packets
        Y_output['deliveryRatio'] = received_packets / sent_packets
        Y_output['dropRatio']= dropped_packets / sent_packets
    elif choice==1:
        Y_output['throughput'] = (received_bytes * 8) / simulation_time
        Y_output['avgDelay'] = total_delay / received_packets
        Y_output['deliveryRatio'] = received_packets / sent_packets
        Y_output['dropRatio']= dropped_packets / sent_packets
    return Y_output


def plotGraph(X_input,Y_output,x_Label,y_Label,title):
    plt.figure(figsize=(7,4))
    plt.plot(X_input, Y_output,color='green',marker='o', markerfacecolor='blue', markersize=10)
   
    # naming the x axis
    plt.xlabel(x_Label)
    # naming the y axis
    plt.ylabel(y_Label)

    # giving a title to my graph
    plt.title(title)

    for i_x, i_y in zip(X_input, Y_output):
        plt.text(i_x, i_y, '({}, {:.2f})'.format(i_x, i_y))

    # function to show the plot
    plt.show()


# def plotGraph2(X_input,Y_output,x_Label,y_Attributes,title):
#    # plt.figure(figsize=(7,4))
#     figure=['f1','f2','f3','f4']
#     count=0;
#     for y_attribute in y_Attributes:
#         #figure[count]=plt.figure(figsize=(7,4))
#         figure[count]=plt.plot(X_input, Y_output[y_attribute],color='green',marker='o', markerfacecolor='blue', markersize=10)

#         # naming the x axis
#         figure[count].xlabel(x_Label)
#         # naming the y axis
#         figure[count].ylabel(y_attribute)

#         # giving a title to my graph
#         figure[count].title('{} {} Vs {}'.format(title,y_attribute,x_Label))

#         for i_x, i_y in zip(X_input, Y_output[y_attribute]):
#             figure[count].text(i_x, i_y, '({}, {:.2f})'.format(i_x, i_y))
#         count = count + 1
#     # function to show the plot
#     plt.show()
