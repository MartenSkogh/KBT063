# Viewing output in Avogadro

Apparently, Orca (atleast on Windows) outputs files in an encoding that is not supported by Avogadro. A work around is to convert the file to ASCII. In Windows Powershell this can be done with 

`orca input_file.inp | Out-File -Encoding ASCII -FilePath output_file.out`

