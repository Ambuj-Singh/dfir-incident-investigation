rule suspicious_syshelper_strings
{
  meta:
    author = "DFIR Analyst"
    description = "Detects strings related to SysHelper sample used in simulation"
    date = "2026-05-06"

  strings:
    $s1 = "SysHelper"
    $s2 = "malware-serve.example.com"
    $s3 = "svc.exe"

  condition:
    any of ($s*)
}
