---
title: "How to set up Jupyter notebook on a remote VM"
description: ""
author: 
 - name: "Hiroshi Doyu"
   email: hiroshi.doyu@ninjalabo.ai
date: "08/17/2024"
draft: false
categories:
  - Tech
---

```
ssh root@gpu-instance-ip
jupyter notebook --no-browser --port=8888 --allow-root
ssh -N -L localhost:7777:localhost:8888 root@gpu-instance-ip
```
https://www.scaleway.com/en/docs/tutorials/setup-jupyter-notebook/


