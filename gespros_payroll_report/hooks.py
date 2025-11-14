def pre_init_hook(env):
    """Drop the legacy payslip asset view that inherited the removed web.report_assets_common."""
    try:
        view = env.ref("gespros_payroll_report.payslip_report_assets", raise_if_not_found=False)
    except ValueError:
        view = False
    if view:
        view.unlink()
