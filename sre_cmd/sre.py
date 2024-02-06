#! /usr/bin/env python3

import argparse
import shutil
import subprocess

kubecmd = shutil.which("kubectl")

if kubecmd == None:
    print("kubectl not found. Please see https://kubernetes.io/docs/tasks/tools/ to install kubectl and/or add it to your $PATH")
    exit(1)


parser = argparse.ArgumentParser()
parser.add_argument("list", nargs="?", help="list deployments in all namespaces")
parser.add_argument("--namespace", help="constrain deployments to this namespace")

parser.add_argument("scale", nargs="?", help="set a new size for a replica or deployment")
parser.add_argument("--replicas", help="new number of replicas")
parser.add_argument("--deployment", help="deployment name")

parser.add_argument("info", nargs="?", help="get info for a resource type")
parser.add_argument("--resource",  choices=["pod", "deployment", "service"] )

args = parser.parse_args()


def listdeploy(namespace):
    kubecmdargs = ["get",  "-A", "deployments"] if namespace == None else ["get", "deployments", "--namespace", namespace]
    subprocess.run([kubecmd] + kubecmdargs)

def scale(replicas, namespace, deployment):
    kubecmdargs = ["scale", "--replicas", replicas, "--namespace", namespace, deployment]
    subprocess.run([kubecmd] + kubecmdargs)

def info(resource, namespace):
    kubecmdargs = ["get",  "-A", resource] if namespace == None else ["get", resource, "--namespace", namespace]
    subprocess.run([kubecmd] + kubecmdargs)

if args.list == "list":
    listdeploy(args.namespace)
    
if args.list == "scale":
    scale(args.replicas, args.namespace, args.deployment)
    
if args.list == "info":
    info(args.resource, args.namespace)