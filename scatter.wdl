version 1.0

workflow reverse_flow {
    input {
       Array[String] inputFiles
    }
    scatter(oneFile in inputFiles) {
    call reverse { input: inputFile=oneFile }
    }


}

task reverse {
    input {
    String inputFile
    }
    command {
        python3 /home/ziygawish/CURIS-workplace/reverse.py ${inputFile}
    }

    output {
        String value = stdout()
    }

}