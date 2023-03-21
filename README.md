# k8s-kopf-sslmonitor-operator
k8s-kopf-sslmonitor-operator checks the expiry date of the given domain and it gives the date of expiry of SSL and the days remaining.

It is build on top of Kubernetes Operator Pythonic Framework (Kopf).

## Requirements
-  kubectl
-  kind or minikube
-  kopf

## Run in Development

- Clone the repository on your local machine
```bash
git clone <url>
cd <to_folder>
```

- Create virtual environment
```bash
python3 -m venv env
```
- Install the required python packages.

```bash
pip3 install -r requirements.txt
```
- Apply the custom resource definition.
```bash
kubectl apply -f crd.yaml
```
- Check whether crd is applied or not.
```bash
kubectl api-resources
```
- Run controller.py in a background.
```bash
kopf run controller.py --verbose
```
- Create a object of the custom resources.
```bash
kubectl apply -f obj.yaml
```
- Check whether the custom resource objects is created or not.

```bash
kubectl get ssl
```
![screenshots](./screenshots/relambda-ssl.png)

## Deploy in Kubernetes 
![Work in Progress](./screenshots/Loading_icon.gif)

Work in Progress !!!