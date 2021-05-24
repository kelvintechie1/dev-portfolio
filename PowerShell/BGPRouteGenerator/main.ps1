# Ensure that your PowerShell code execution policy is set correctly - Set-ExecutionPolicy -ExecutionPolicy Unrestricted
# Install Routing sub-role first - uncomment the following line to install it. NOTE: This requires a restart, automatically done with the -Restart flag.

# Install-WindowsFeature RemoteAccess -IncludeAllSubFeature -IncludeManagementTools -Restart -Verbose

# Create a variable to hold BGP routes
$bgpRoutes = @()

# Create operational variables - comments after each to indicate their purpose
$numberOfRoutes = 10 # Determines number of routes to generate
$minimumPrepend = 0 # Determines minimum number of ASNs to prepend in AS-PATH
$maximumPrepend = 0 # Determines maximum number of ASNs to prepend in AS-PATH
$includeZero = $false # Determine whether to include 0.0.0.0/<prefixLength> prefixes or not (i.e. 0.0.0.0/1)
$minimumPLength = 8 # Determines minimum prefix length (recommended: at least 8, especially if includeZero is False, increase from 0 for default-free BGP route generation)
$maximumPLength = 32 # Determines maximum prefix length (recommended: 32, lower if you want host address-free advertisements)


# Generate random prefixes between 0.0.0.0 or 1.0.0.0 and 223.255.255.255, with a prefix length between /8 and /32
for ($i = 0; $i -lt $numberOfRoutes; $i++) {
    $decimalPrefix = 0
    if ($includeZero -eq $true) {
        $decimalPrefix = Get-Random -Minimum 0 -Maximum 3758096383
    }
    elseif ($includeZero -eq $false) {
        $decimalPrefix = Get-Random -Minimum 16777216 -Maximum 3758096383
    }
    $PL = Get-Random -Minimum $minimumPLength -Maximum $maximumPLength
    $prefix = (New-Object System.Net.IPAddress($decimalPrefix)).ToString()
    $bgpRoutes = $bgpRoutes + ($prefix + "/" + $PL.ToString())
}

$bgpRoutes | ForEach-Object { 
    Add-BgpCustomRoute -Network $_
    Write-Host $_ successfully added as a BGP custom route! 
}
