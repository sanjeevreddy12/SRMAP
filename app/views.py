from django.shortcuts import render
import os
import datetime
from django.http import HttpResponse
import subprocess

def htop_view(request):
    name = "Sanjeev Reddy"
    username = os.getenv("USER", "Unknown")
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    top_output = subprocess.getoutput("top -b -n 1 | head -10")
    response = f"""
    <h1>System Info</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time:</strong> {server_time} IST</p>
    <pre>{top_output}</pre>
    """
    return HttpResponse(response)
# Create your views here.
