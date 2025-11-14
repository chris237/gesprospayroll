from odoo import SUPERUSER_ID, api


def pre_init_hook(cr):
    """Drop the legacy payslip asset view that inherited the removed web.report_assets_common."""
    env = api.Environment(cr, SUPERUSER_ID, {})
    try:
        view = env.ref("gespros_payroll_report.payslip_report_assets", raise_if_not_found=False)
    except ValueError:
        view = False
    if view:
        view.unlink()
