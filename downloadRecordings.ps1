# https://archive.liveatc.net/kjfk/KJFK-Twr-Jun-24-2024-0000Z.mp3

$baseUrl = "https://archive.liveatc.net/kjfk/KJFK-Twr-Jun-24-2024-"

# Initialize time as a string
$time = "0000"

$client = New-Object System.Net.WebClient

# Loop until time is less than 24 hours
while ($time -ne "2330") {
	$url = $baseUrl + $time + "Z.mp3"

	Write-Output "Downloading $url"

	try {
		# Download the file
		$client.DownloadFile($url, "/home/rodoggx/iResearch-2024/ATC-recordings/KJFK-Twr-Jun-24-2024-" + $time + "Z.mp3")
	} catch {
		Write-Output "File not found"
	}
    # Convert string to DateTime object for easy manipulation
    $timeObject = [DateTime]::ParseExact($time, "HHmm", $null)

    # Add 30 minutes
    $timeObject = $timeObject.AddMinutes(30)

    # Convert DateTime object back to string
    $time = $timeObject.ToString("HHmm")

    # Output the time
    # Write-Output $time
}
