#!/usr/bin/env python3

import os
import time

# You need to clone your repository first to the server. You may use this command:

#git clone https://[your_username]:[your_private_token]@github.com/user/repo /path/to/folder")

def update_from_repo():
    try:
        os.system("git -C /path/to/folder pull")
        time.sleep(0.5)
        delete_container()
    except Exception as e:
        print(e)
        
def delete_container():
    try:
        os.system("docker stop [container_name] && docker rm [container_name]") # Replace [container_name] with the name of your container
        time.sleep(0.5)
        os.system("docker image rm [image_name]") # Replace [image_name] with the name of your docker image
        time.sleep(0.5)      
        build_image()
    except Exception as e:
        print(e)
    
def build_image():
    try:
        os.system("docker build -t [container_name] path/to/folder") # Replace [container_name] with the name of your container
        time.sleep(0.5)
        run_container()
    except Exception as e:
        print(e)

def run_container():
    try:
        os.system("docker run -d --name [container_name] --restart=unless-stopped --network=[your_docker_network]  [your_image_name]") # Replace [container_name] with the name of your container, [your_docker_network] with the name of your docker network and [your_image_name] with the name of your docker image
        time.sleep(0.5)
        write_log()
        
    except Exception as e:
        print(e)

def write_log():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    with open("pageupdate.log", "a") as file:
        file.write(current_time + " Website update successful" + "\n")
    print(">>> Website update successful -- " + current_time)

if __name__ == "__main__":
    update_from_repo()
    
