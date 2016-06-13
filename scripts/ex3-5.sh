#! /bin/bash

func()
{
    local v1=200
    echo $v1
}
v1=100
func
echo $v1
