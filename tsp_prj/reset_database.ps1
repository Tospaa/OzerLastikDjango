$yes=New-Object System.Management.Automation.Host.ChoiceDescription "&Yes", "Deletes the database and app migrations."
$no=New-Object System.Management.Automation.Host.ChoiceDescription "&No", "Exits the script."

$options = [System.Management.Automation.Host.ChoiceDescription[]]($yes, $no)

$result = $host.ui.PromptForChoice("Database Deletion Script", "Are you really sure to reset the database?", $options, 1)

if (!$result)
{
    Remove-Item -Force .\db.sqlite3
    Remove-Item -Recurse -Force .\api\migrations
    Remove-Item -Recurse -Force .\dashboard\migrations
    .\migration.ps1
    python .\manage.py createsuperuser --username Tospaa --email musaecer@gmail.com
} elseif ($result) {
    exit
}