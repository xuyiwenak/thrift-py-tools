#!/usr/bin/env bash
set -e

PWD=$(cd `dirname ${0}`; pwd)
IMG="thrift"
# 支持的语言可以根据情况自己调整
lang_list=(py java js)

if [[ $# != 1 ]]; then
    echo $#
    echo "you must choose a dir for proto."
fi
if [[ ! -d $1 ]]; then
    ls
    echo "$1 does not exists in this dir."
fi

for lang in ${lang_list[*]}
do
    if [[ -d ${PWD}/${lang} ]];then
    #echo ${PWD}/${lang}
    rm -rf ${PWD}/${lang}
    fi
    mkdir ${PWD}/${lang}
    if [[ "${lang}" == "py" ]];then
    touch ${PWD}/${lang}/__init__.py
    fi
done

function read_dir(){
        for file in `ls $1`
        do
            if [[ -d $1"/"$file ]]  #注意此处之间一定要加上空格，否则会报错
            then
                read_dir $1"/"$file
            else
                # 取文件后缀
                extension=${file##*.}
                if [[ ${extension} == "thrift" ]]
                then
                    docker run --rm -it -v $PWD:/data ${IMG} thrift -o /data/$2 --gen $2 /data/protos/${file}
                fi
            fi
        done
    }

for lang in ${lang_list[*]}
do
    read_dir $1 ${lang}
    if [[ -d ${PWD}/${lang}/gen_${lang} ]]; then
        echo ${PWD}/${lang}/gen_${lang}
        rm -rf ${PWD}/${lang}/gen_${lang}
    fi
    mv "${PWD}/${lang}/gen-${lang}" "${PWD}/${lang}/gen_${lang}"
done


