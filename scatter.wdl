version 1.0

workflow reverse_flow {

    Array[File] inputFiles

    scatter (oneFile in inputFiles) {
    call reverse { input: inputFile=oneFile }
    }


}

task reverse {
    File inputFile

    command {
        python reverse.py ${inputFile}
    }

    output {
        File value = "result.txt"
    }

}