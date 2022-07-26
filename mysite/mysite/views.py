# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 13:12:31 2022

@author: Ayush Lath
"""

# I have created this file - AYUSH LATH

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    with open("1.txt") as f:
        return HttpResponse(f.read())
    
def about(request):
    
    return render(request,'index.html')
    
def ex1(request):
    
    s=''' <h2>Navigation Bar<br></h2>
    <a href = "https://www.youtube.com/c/CodeHelpbyBabbar/playlists">Love Babbar Playlist<br>
    <a href = "https://leetcode.com/Ayush_lath/">Ayush Lath Leetcode Profile<br>
    <a href = "https://auth.geeksforgeeks.org/user/ayushlath/practice/">Ayush Lath GFG Profile<br>
    '''
    return HttpResponse(s)

# Starting Code to learn 
def analyze(request):
    djtext = request.POST.get('text','off')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlinerem = request.POST.get('newlinerem','off')
    spacerem = request.POST.get('spacerem','off')
    charcnt = request.POST.get('charcnt','off')
    st=djtext
    
    if removepunc == "on":
        analyzed =""
        punctuations = '''!()[]{}-;:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose':'remove','analyze_text':analyzed}
        st = analyzed
        
    if fullcaps=="on":
        analyzed=""
        for char in st:
            analyzed = analyzed+char.upper()
        st = analyzed
        params = {'purpose':'Upper Case','analyze_text':analyzed}
        
    if newlinerem=="on":
        analyzed=""
        for char in st:
            if char!='\n' and char!='\r':
                analyzed = analyzed+char
        params = {'purpose':'New Line Remove','analyze_text':analyzed}
        st = analyzed
        
    if spacerem=="on":
        analyzed=""
        for char in st:
            if char!='  ':
                analyzed = analyzed+char
        params = {'purpose':'Space Remove','analyze_text':analyzed}
        st=analyzed
        
    if charcnt=="on":
        analyzed=0
        for char in djtext:
            if char!=' ':
                analyzed = analyzed+1
        params = {'purpose':'Char Count','analyze_text':analyzed}
        st = analyzed
        
    params = {'purpose':'Compute all checkbox','analyze_text':st}
    if removepunc=="on" or fullcaps=="on" or newlinerem=="on" or spacerem=="on" or charcnt=="on" :
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error. Please select the button to perform operation")

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newline remove first")


# def spaceremove(request):
#     return HttpResponse("space remover back")

# def charcount(request):
#     return HttpResponse("charcount ")

# def about(request):
#     return HttpResponse('hello Ayush')