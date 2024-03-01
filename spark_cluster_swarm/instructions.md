# Spark Cluster Swarm Setup Instructions

Follow these steps to set up a Spark cluster using Docker Swarm:

1. **Create the instances and install Docker on them:**
    - Provision the required instances for your Spark cluster.
    - Install Docker on each instance.

2. **Initialize one of the instances as the Swarm manager:**
    - Choose one of the instances to act as the Swarm manager.
    - Run the command `docker swarm init` on the chosen instance to initialize it as the Swarm manager.

3. **Join the worker instance to the Swarm manager:**
    - On the worker instance, run the command provided by the Swarm manager after the initialization process.
    - This will join the worker instance to the Swarm manager.

4. **Create a Docker network:**
    - Run the command `docker network create --driver overlay spark_network` to create a Docker network for the Spark cluster.

5. **Create a Docker Compose file:**
    - Create a Docker Compose file (e.g., `docker-compose.yml`) with the necessary configurations for your Spark service.
    - Specify the desired number of replicas for the Spark service.

6. **Deploy the Spark service:**
    - Run the command `docker stack deploy -c docker-compose.yml spark_cluster` to deploy the Spark service on the Swarm cluster.

7. **Access the Spark UI:**
    - Open a web browser and navigate to the URL `http://<manager-instance-ip>:8080` to access the Spark UI.
    - Replace `<manager-instance-ip>` with the IP address of the Swarm manager instance, in our case the `Floating IP`.

8. **Submit a Spark job:**
    - Use the Spark UI or the `spark-submit` command to submit a Spark job to the cluster.