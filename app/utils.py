import json
import matplotlib.pyplot as plt


def get_data_from_json(filepath):
    with open(filepath) as file:
        data = json.load(file)
    return data


def plot_graph(power_data):
    timestamps = [data.timestamp for data in power_data]
    values = [data.value for data in power_data]

    plt.plot(timestamps, values)
    plt.xlabel('Timestamp')
    plt.ylabel('Power Value')
    plt.title('Power Usage Graph')

    # Save the plot to a file
    graph_filepath = '/path/to/save/graph.png'
    plt.savefig(graph_filepath)
    plt.close()

    return graph_filepath
