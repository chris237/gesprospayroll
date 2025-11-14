{
    "name": "GESPROS Payroll Payslip",
    "version": "18.0.1.0.0",
    "summary": "Custom payslip layout inspired by GESPROS template",
    "description": """Replaces the native payroll payslip report with a branded layout.""",
    "category": "Human Resources/Payroll",
    "depends": [
        "web",
        "hr_payroll",
    ],
    "data": [
        "report/assets.xml",
        "report/payslip_templates.xml",
    ],
    "assets": {},
    "license": "LGPL-3",
    "author": "GESPROS",
    "website": "https://www.gespros.com",
    "application": False,
    "installable": True,
    "pre_init_hook": "pre_init_hook",
}
