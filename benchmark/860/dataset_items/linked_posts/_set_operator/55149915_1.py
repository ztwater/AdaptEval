---
apiVersion: v1
kind: Pod
metadata:
  name: fail-422f98fc
  labels: {}
  annotations: {}
spec:
  containers:
  - name: base
    image: python:3.6.6-stretch
    command: ['echo']
    imagePullPolicy: IfNotPresent
    args: ['10']
  restartPolicy: Never
  nodeSelector: {}
  volumes: []
  serviceAccountName: default
  affinity: {}
