### kubernetes








### 查看状态 cp diff port update ps
  docker container inspect test  
  docker container cp data test:/tmp/
  docker port nostalgic_morse 5000
  docker container update 
    更新一些运行时配置，主要是资源限制份额
  docker ps 查看容器的连接


  HAProxy
  



### docker 网络

#### 端口映射

  docker run -d -p 127.0.0.1:5000:5000 training/webapp python app.py

#### 容器互联

  docker run -d -P --name web --link db:db training/webapp python app.py


#### 跨主机通信 libnetwork （SDN NFV）

  





### docker 数据

  数据卷 数据卷容器

  docker run -d -P --name web -v /webapp xxxx python app.py(创建数据卷)
  docker run -d -P --name web -v /local/webapp:/contain/webapp xxxx python app.py
    -v /local/webapp:/contain/webapp:ro(默认读写权限)

  容器之间共享数据(数据卷容器，拿一个单独的容器当数据卷,不需要保持运行状态)
      docker run -it -v /dbdata --name dbdata ubuntu
      docker run -it --volumes-from dbdata --name db1 ubuntu
      docker run -it --volumes-from dbdata --name db2 ubuntu
      docker run -d --name db3 --volumes-from dbdata db1 ubuntu(dbdata>db1>db3传递挂载数据卷)

  数据卷容器迁移数据：基于文件夹的数据备份，恢复(容器内外运行)
    tar -cvf xx.tar xx/dbdata






### Dockerfile 创建镜像

### vmware workstation + CoreOS


### 守护态运行

  docker run -d ubuntu /bin/sh "while true; do echo hello; sleep 1; done";

  sudo docker logs xxxx






### 容器管理 从镜像 容器 运行 
  docker ps -a

  docker run -it ubuntu bash  (4a1068c164bd)
    docker exec -ti 4a1068c164bd bash（新终端）

  docker attack 4a1068c164bd （同一个终端）

  docker start|stop|restart 4a1068c164bd

    docker rm  4a1068c164bd(永久删除容器)
  
  docker create -it ubuntu:lasest (处于停止状态)
  
  docker ps / docker ps --all

  导出容器（含状态,）
    docker export -o test_ubuntu_c.tar  4a1068c164bd
    docker import  test_ubuntu_c.tar - test/ubuntu:v1.0










### 镜像管理  从容器创建自定义镜像 docker 

  docker images ls   
  docker pull xxxx
    docker search xxxx
  docker save | docker load

  docker rmi xxxx(永久删除镜像)

  docker commit -m "aaaa" -a "jc" dd36d68c040c testUbuntu

  docker save -o ubuntutest.tar test-ubuntu
  docker load --input ubuntutest.tar
  
  docker save | docker load

  注册dockerhub后，可以上传镜像
      docker tag docker push
  



### 容器镜像下载

  docker pull ubuntu
  docker search mysql




### jc@dock:~$ docker --help

Usage:	docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Options:
      --config string      Location of client config files (default "/home/jc/.docker")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket(s) to connect to
  -l, --log-level string   Set the logging level ("debug"|"info"|"warn"|"error"|"fatal") (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default "/home/jc/.docker/ca.pem")
      --tlscert string     Path to TLS certificate file (default "/home/jc/.docker/cert.pem")
      --tlskey string      Path to TLS key file (default "/home/jc/.docker/key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Management Commands:
  builder     Manage builds
  config      Manage Docker configs
  container   Manage containers
  engine      Manage the docker engine
  image       Manage images
  network     Manage networks
  node        Manage Swarm nodes
  plugin      Manage plugins
  secret      Manage Docker secrets
  service     Manage services
  stack       Manage Docker stacks
  swarm       Manage Swarm
  system      Manage Docker
  trust       Manage trust on Docker images
  volume      Manage volumes

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  build       Build an image from a Dockerfile
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  images      List images
  import      Import the contents from a tarball to create a filesystem image
  info        Display system-wide information
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  login       Log in to a Docker registry
  logout      Log out from a Docker registry
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  ps          List containers
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  run         Run a command in a new container
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  search      Search the Docker Hub for images
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  version     Show the Docker version information
  wait        Block until one or more containers stop, then print their exit codes







### 安装

sudo apt-get install docker-ce

sudo docker run hello-world



## env tools
 centos
```
  yum install net-tools
  yum -y install initscripts
```


