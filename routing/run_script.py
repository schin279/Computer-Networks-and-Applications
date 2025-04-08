import time
import random
import subprocess

def generate_network(num_nodes):
    # Generate a random network with num_nodes and random links
    network_str = ""
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random.random() < 0.3:  # Adjust the probability of having a link
                cost = random.randint(1, 10)  # Random cost between 1 and 10
                network_str += f"{i}-{j}-{cost}\n"
    return network_str.strip()

def run_dijkstra(input_str, algorithm):
    start_time = time.time()
    process = subprocess.Popen([algorithm], stdout=subprocess.PIPE, stdin=subprocess.PIPE, text=True)
    out, _ = process.communicate(input=input_str)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

def main():
    num_nodes_list = [10, 50, 100, 150]  # Number of nodes for each data point
    num_links_list = []
    execution_time_n2_list = []
    execution_time_nlogn_list = []

    for num_nodes in num_nodes_list:
        network_str = generate_network(num_nodes)
        num_links = network_str.count('\n') + 1  # Counting the number of links
        num_links_list.append(num_links)

        # Run Dijkstra's algorithm with N*N complexity
        execution_time_n2 = run_dijkstra(network_str, "./Dijkstra")
        execution_time_n2_list.append(execution_time_n2)

        # Run Dijkstra's algorithm with N*log(N) complexity
        execution_time_nlogn = run_dijkstra(network_str, "./DijkstraNlogN")
        execution_time_nlogn_list.append(execution_time_nlogn)

    # Print summary table
    print("For Dijkstra with N * N complexity\n")
    print("    Number of Nodes     Number of Links     Execution Time (N*N) ")
    for i in range(len(num_nodes_list)):
        print(f"    {num_nodes_list[i]}{' ' * (19 - len(str(num_nodes_list[i])))} {num_links_list[i]}{' ' * (18 - len(str(num_links_list[i])))}  {execution_time_n2_list[i]}{' ' * (22 - len(str(execution_time_n2_list[i])))}")

    print("\nFor Dijkstra with N log N complexity\n")
    print("    Number of Nodes     Number of Links     Execution Time (N log N)")
    for i in range(len(num_nodes_list)):
        print(f"    {num_nodes_list[i]}{' ' * (19 - len(str(num_nodes_list[i])))} {num_links_list[i]}{' ' * (18 - len(str(num_links_list[i])))}  {execution_time_nlogn_list[i]}{' ' * (22 - len(str(execution_time_nlogn_list[i])))}")

if __name__ == "__main__":
    main()