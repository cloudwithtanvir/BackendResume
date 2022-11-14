source /home/tanvir/Desktop/wp/djnago-react/venv/bin/activate



# Django Backend


## Build the docker 

sudo docker build -t eks-demo .

sudo aws ecr get-login-password --region ap-southeast-1 |sudo docker login --username AWS --password-stdin 695443029058.dkr.ecr.ap-southeast-1.amazonaws.com

### Run the docker locally 

sudo docker run --name resume -d -p 8000:8000 resume:latest

docker tag eks-demo:latest 695443029058.dkr.ecr.ap-southeast-1.amazonaws.com/eks-demo:latest

sudo docker push 695443029058.dkr.ecr.ap-southeast-1.amazonaws.com/eks-demo:latest