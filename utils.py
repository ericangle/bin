#!/usr/bin/python

import os
import sys

def runShellCommand(command):
  os.system(command)

def getOutputOfShellCommandAsList(command):
  return os.popen(command).read().splitlines()

def getEnvironmentVariable(variable):
  return getOutputOfShellCommandAsList('echo $' + variable)[0]

def environmentVariableIsSet(variable):
  return getEnvironmentVariable(variable) != ''

def directoryExists(directory):
  return os.path.isdir(directory)

def createDirectoryIfItDoesntExist(directory):
  if not directoryExists(directory):
    os.system('mkdir -p ' + directory)

def removeDirectoryIfItExists(directory):
  if directoryExists(directory):
    os.system('rm -r ' + directory)

def getLinesOfFile(fileName):
  return [line.split('\n')[0] for line in open(fileName,'r').readlines()]

def getFileNameWithoutPathOrExtension(fileNameWithPathOrExtension):
  return fileNameWithPathOrExtension.split('/')[-1].split('.')[0]

def exitWithMessage(message):
  sys.exit(message)

def printHeader(header,numEachSide):
  length = len(header) + 2*(numEachSide + 1)
  print ' '
  print length*'-'
  print numEachSide*' ' + ' ' + header + ' ' + numEachSide*' '
  print length*'-'
  print ' '
