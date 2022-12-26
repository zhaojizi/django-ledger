"""
Django Ledger created by Miguel Sanda <msanda@arrobalytics.com>.
Copyright© EDMA Group Inc licensed under the GPLv3 Agreement.

Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Pranav P Tulshyan <ptulshyan77@gmail.com>
"""

"""
This is the base Chart of Accounts that has all the possible accounts that are useful for the prepeartion of the Financial Statements.

The Chart of Accounts is Braodly Bifurcted into 5 different Sections:

1. Assets:
2. Liabilities
3. Shareholder's Equity
4. Expenses 
5. Revenue
"""


from itertools import groupby

from django_ledger.io import roles
from django.utils.translation import gettext_lazy as _

CHART_OF_ACCOUNTS = [

    # ---------# ASSETS START #---------#
    # CURRENT ASSETS  ------
    {'code': '1010', 'role': roles.ASSET_CA_CASH, 'balance_type': 'debit', 'name': _('Cash'), 'parent': None},
    {'code': '1050', 'role': roles.ASSET_CA_MKT_SECURITIES, 'balance_type': 'debit', 'name': _('Short Term Investments'), 'parent': None},
    {'code': '1100', 'role': roles.ASSET_CA_RECEIVABLES, 'balance_type': 'debit', 'name': _('Accounts Receivable'), 'parent': None},
    {'code': '1110', 'role': roles.ASSET_CA_UNCOLLECTIBLES, 'balance_type': 'credit', 'name': _('Uncollectibles'), 'parent': None},
    {'code': '1200', 'role': roles.ASSET_CA_INVENTORY, 'balance_type': 'debit', 'name': _('Inventory'), 'parent': None},
    {'code': '1300', 'role': roles.ASSET_CA_PREPAID, 'balance_type': 'debit', 'name': _('Prepaid Expenses'), 'parent': None},

    # LONG TERM INVESTMENTS ------
    {'code': '1510', 'role': roles.ASSET_LTI_NOTES_RECEIVABLE, 'balance_type': 'debit', 'name': _('Notes Receivable'), 'parent': None},
    {'code': '1520', 'role': roles.ASSET_LTI_LAND, 'balance_type': 'debit', 'name': _('Land'), 'parent': None},
    {'code': '1530', 'role': roles.ASSET_LTI_SECURITIES, 'balance_type': 'debit', 'name': _('Securities'), 'parent': None},

    # PPE ------
    {'code': '1610', 'role': roles.ASSET_PPE_BUILDINGS, 'balance_type': 'debit', 'name': _('Buildings'), 'parent': None},
    {'code': '1611', 'role': roles.ASSET_PPE_BUILDINGS_ACCUM_DEPRECIATION, 'balance_type': 'credit', 'name': _('Less: Buildings Accumulated Depreciation'), 'parent': None},
    {'code': '1620', 'role': roles.ASSET_PPE_PLANT, 'balance_type': 'debit', 'name': _('Plant'), 'parent': None},
    {'code': '1621', 'role': roles.ASSET_PPE_PLANT_ACCUM_DEPRECIATION, 'balance_type': 'credit', 'name': _('Less: Plant Accumulated Depreciation'), 'parent': None},
    {'code': '1630', 'role': roles.ASSET_PPE_EQUIPMENT, 'balance_type': 'debit', 'name': _('Equipment'), 'parent': None},
    {'code': '1631', 'role': roles.ASSET_PPE_EQUIPMENT_ACCUM_DEPRECIATION, 'balance_type': 'credit', 'name': _('Less: Equipment Accumulated Depreciation'), 'parent': None},
    {'code': '1640', 'role': roles.ASSET_PPE_PLANT, 'balance_type': 'debit', 'name': _('Vehicles'), 'parent': None},
    {'code': '1641', 'role': roles.ASSET_PPE_PLANT_ACCUM_DEPRECIATION, 'balance_type': 'credit', 'name': _('Less: Vehicles Accumulated Depreciation'), 'parent': None},
    {'code': '1650', 'role': roles.ASSET_PPE_PLANT, 'balance_type': 'debit', 'name': _('Furniture & Fixtures'), 'parent': None},
    {'code': '1651', 'role': roles.ASSET_PPE_PLANT_ACCUM_DEPRECIATION, 'balance_type': 'credit', 'name': _('Less: Furniture & Fixtures Accumulated Depreciation'), 'parent': None},

    # INTANGIBLE ASSETS ------
    {'code': '1810', 'role': roles.ASSET_INTANGIBLE_ASSETS, 'balance_type': 'debit', 'name': _('Goodwill'), 'parent': None},
    {'code': '1820', 'role': roles.ASSET_INTANGIBLE_ASSETS, 'balance_type': 'debit', 'name': _('Intellectual Property'), 'parent': None},
    {'code': '1830', 'role': roles.ASSET_INTANGIBLE_ASSETS_ACCUM_AMORTIZATION, 'balance_type': 'credit', 'name': _('Less: Intangible Assets Accumulated Amortization'), 'parent': '1820'},

    # ADJUSTMENTS ------
    {'code': '1910', 'role': roles.ASSET_ADJUSTMENTS, 'balance_type': 'debit', 'name': _('Securities Unrealized Gains/Losses'), 'parent': None},
    {'code': '1920', 'role': roles.ASSET_ADJUSTMENTS, 'balance_type': 'debit', 'name': _('PPE Unrealized Gains/Losses'), 'parent': None},

    # ---------# ASSETS END #---------#

    # ---------# LIABILITIES START #---------#
    # CURRENT LIABILITIES ------
    {'code': '2010', 'role': roles.LIABILITY_CL_ACC_PAYABLE, 'balance_type': 'credit', 'name': _('Accounts Payable'), 'parent': None},
    {'code': '2020', 'role': roles.LIABILITY_CL_WAGES_PAYABLE, 'balance_type': 'credit', 'name': _('Wages Payable'), 'parent': None},
    {'code': '2030', 'role': roles.LIABILITY_CL_INTEREST_PAYABLE, 'balance_type': 'credit', 'name': _('Interest Payable'), 'parent': None},
    {'code': '2040', 'role': roles.LIABILITY_CL_ST_NOTES_PAYABLE, 'balance_type': 'credit', 'name': 'Short-Term Notes Payable', 'parent': None},
    {'code': '2050', 'role': roles.LIABILITY_CL_LTD_MATURITIES, 'balance_type': 'credit', 'name': _('Current Maturities LT Debt'), 'parent': None},
    {'code': '2060', 'role': roles.LIABILITY_CL_DEFERRED_REVENUE, 'balance_type': 'credit', 'name': _('Deferred Revenues'), 'parent': None},
    {'code': '2070', 'role': roles.LIABILITY_CL_OTHER, 'balance_type': 'credit', 'name': _('Other Payables'), 'parent': None},

    # LIABILITIES ACCOUNTS ------
    {'code': '2110', 'role': roles.LIABILITY_LTL_NOTES_PAYABLE, 'balance_type': 'credit', 'name': _('Long Term Notes Payable'), 'parent': None},
    {'code': '2120', 'role': roles.LIABILITY_LTL_BONDS_PAYABLE, 'balance_type': 'credit', 'name': _('Bonds Payable'), 'parent': None},
    {'code': '2130', 'role': roles.LIABILITY_LTL_MORTGAGE_PAYABLE, 'balance_type': 'credit', 'name': _('Mortgage Payable'), 'parent': None},

    # ---------# LIABILITIES END #---------#

    # ---------# SHEREHOLDERS EQUITY START #---------#
    # CAPITAL ACCOUNTS ------
    {'code': '3010', 'role': roles.EQUITY_CAPITAL, 'balance_type': 'credit', 'name': _('Capital Account 1'), 'parent': None},
    {'code': '3020', 'role': roles.EQUITY_CAPITAL, 'balance_type': 'credit', 'name': _('Capital Account 2'), 'parent': None},
    {'code': '3030', 'role': roles.EQUITY_CAPITAL, 'balance_type': 'credit', 'name': _('Capital Account 3'), 'parent': None},

    {'code': '3110', 'role': roles.EQUITY_COMMON_STOCK, 'balance_type': 'credit', 'name': _('Common Stock'), 'parent': None},
    {'code': '3120', 'role': roles.EQUITY_PREFERRED_STOCK, 'balance_type': 'credit', 'name': _('Preferred Stock'), 'parent': None},

    {'code': '3910', 'role': roles.EQUITY_ADJUSTMENT, 'balance_type': 'credit', 'name': _('Available for Sale'), 'parent': None},
    {'code': '3920', 'role': roles.EQUITY_ADJUSTMENT, 'balance_type': 'credit', 'name': _('PPE Unrealized Gains/Losses'), 'parent': None},

    {'code': '3930', 'role': roles.EQUITY_DIVIDENDS, 'balance_type': 'debit', 'name': _('Dividends & Distributions'), 'parent': None},

    # REVENUE ACCOUNTS ------
    {'code': '4010', 'role': roles.INCOME_OPERATIONAL, 'balance_type': 'credit', 'name': _('Sales Income'), 'parent': None},
    {'code': '4020', 'role': roles.INCOME_INVESTING, 'balance_type': 'credit', 'name': _('Investing Income'), 'parent': None},
    {'code': '4030', 'role': roles.INCOME_INTEREST, 'balance_type': 'credit', 'name': _('Interest Income'), 'parent': None},
    {'code': '4040', 'role': roles.INCOME_CAPITAL_GAIN_LOSS, 'balance_type': 'credit', 'name': _('Capital Gain/Loss Income'), 'parent': None},
    {'code': '4050', 'role': roles.INCOME_OTHER, 'balance_type': 'credit', 'name': _('Other Income'), 'parent': None},

    # COGS ACCOUNTS ------
    {'code': '5010', 'role': roles.COGS, 'balance_type': 'debit', 'name': _('Cost of Goods Sold'), 'parent': None},

    # EXPENSE ACCOUNTS ------
    {'code': '6010', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Advertising'), 'parent': None},
    {'code': '6020', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Amortization'), 'parent': None},
    {'code': '6030', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Auto Expense'), 'parent': None},
    {'code': '6040', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Bad Debt'), 'parent': None},
    {'code': '6050', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Bank Charges'), 'parent': None},
    {'code': '6060', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Commission Expense'), 'parent': None},
    {'code': '6080', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Employee Benefits'), 'parent': None},
    {'code': '6090', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Freight'), 'parent': None},
    {'code': '6110', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Gifts'), 'parent': None},
    {'code': '6120', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Insurance'), 'parent': None},
    {'code': '6140', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Professional Fees'), 'parent': None},
    {'code': '6150', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('License Expense'), 'parent': None},
    {'code': '6170', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Maintenance Expense'), 'parent': None},
    {'code': '6180', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Meals & Entertainment'), 'parent': None},
    {'code': '6190', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Office Expense'), 'parent': None},
    {'code': '6220', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Printing'), 'parent': None},
    {'code': '6230', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Postage'), 'parent': None},
    {'code': '6240', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Rent'), 'parent': None},
    {'code': '6250', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Maintenance & Repairs'), 'parent': None},
    {'code': '6251', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Maintenance'), 'parent': None},
    {'code': '6252', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Repairs'), 'parent': None},
    {'code': '6253', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('HOA'), 'parent': None},
    {'code': '6254', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Snow Removal'), 'parent': None},
    {'code': '6255', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Lawn Care'), 'parent': None},
    {'code': '6260', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Salaries'), 'parent': None},
    {'code': '6270', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Supplies'), 'parent': None},
    {'code': '6290', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Utilities'), 'parent': None},
    {'code': '6292', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Sewer'), 'parent': None},
    {'code': '6293', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Gas'), 'parent': None},
    {'code': '6294', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Garbage'), 'parent': None},
    {'code': '6295', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Electricity'), 'parent': None},
    {'code': '6300', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Property Management'), 'parent': None},
    {'code': '6400', 'role': roles.EXPENSE_REGULAR, 'balance_type': 'debit', 'name': _('Vacancy'), 'parent': None},


    {'code': '6070', 'role': roles.EXPENSE_DEPRECIATION, 'balance_type': 'debit', 'name': _('Depreciation Expense'), 'parent': None},
    {'code': '6075', 'role': roles.EXPENSE_AMORTIZATION, 'balance_type': 'debit', 'name': _('Amortization Expense'), 'parent': None},
    {'code': '6130', 'role': roles.EXPENSE_INTEREST, 'balance_type': 'debit', 'name': _('Interest Expense'), 'parent': None},
    {'code': '6210', 'role': roles.EXPENSE_TAXES, 'balance_type': 'debit', 'name': _('Payroll Taxes'), 'parent': None},
    {'code': '6280', 'role': roles.EXPENSE_TAXES, 'balance_type': 'debit', 'name': _('Taxes'), 'parent': None},
    {'code': '6500', 'role': roles.EXPENSE_OTHER, 'balance_type': 'debit', 'name': _('Misc. Expense'), 'parent': None}

]


def verify_unique_code():
    code_list = list(i['code'] for i in CHART_OF_ACCOUNTS)
    code_list.sort()
    code_gb = groupby(code_list)
    return {
        code: sum([bool(v) for v in l]) for code, l in code_gb
    }
