$url = $args[0]

if ($url -eq $null){
    Write-Host "No URL was passed."
    $url =  Read-Host "Please enter the haveibeenpwned.com URL`nShould look like this -  https://haveibeenpwned.com/DomainSearch/<URI>/json`n"
}

$tp = Test-Path .\hibp.json
if ($tp -eq $true){
    Remove-Item .\hibp.json | Out-Null
}

write-host "Pulling JSON file..."
Invoke-RestMethod $url -outfile hibp.json