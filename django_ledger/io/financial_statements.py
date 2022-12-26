from django.core.exceptions import ValidationError

from django_ledger.io.io_context import GroupManager
from django_ledger.io.roles import ASSET_CA_CASH
from django_ledger.models.utils import lazy_loader
from django.utils.translation import gettext_lazy as _


class CashFlowStatementError(ValidationError):
    pass


class CashFlowStatement:
    CFS_DIGEST_KEY = 'cash_flow_statement'

    def __init__(self,
                 io_digest: dict,
                 by_period: bool = False,
                 by_unit: bool = False):
        self.IO_DIGEST = io_digest
        self.CASH_ACCOUNTS = [a for a in self.IO_DIGEST['accounts'] if a['role'] == ASSET_CA_CASH]
        self.JE_MODEL = lazy_loader.get_journal_entry_model()

    def check_io_digest(self):
        if GroupManager.GROUP_BALANCE_KEY not in self.IO_DIGEST:
            raise CashFlowStatementError(
                'IO Digest must have groups for Cash Flow Statement'
            )

    def operating(self):
        group_balances = self.IO_DIGEST[GroupManager.GROUP_BALANCE_KEY]
        operating_activities = dict()
        operating_activities['GROUP_CFS_NET_INCOME'] = {
            'description': _('Net Income'),
            'balance': group_balances['GROUP_CFS_NET_INCOME']
        }
        operating_activities['GROUP_CFS_OP_DEPRECIATION_AMORTIZATION'] = {
            'description': _('Depreciation & Amortization of Assets'),
            'balance': -group_balances['GROUP_CFS_OP_DEPRECIATION_AMORTIZATION']
        }
        operating_activities['GROUP_CFS_OP_INVESTMENT_GAINS'] = {
            'description': _('Gain/Loss Sale of Assets'),
            'balance': group_balances['GROUP_CFS_OP_INVESTMENT_GAINS']
        }
        operating_activities['GROUP_CFS_OP_ACCOUNTS_RECEIVABLE'] = {
            'description': _('Accounts Receivable'),
            'balance': -group_balances['GROUP_CFS_OP_ACCOUNTS_RECEIVABLE']
        }
        operating_activities['GROUP_CFS_OP_INVENTORY'] = {
            'description': _('Inventories'),
            'balance': -group_balances['GROUP_CFS_OP_INVENTORY']
        }

        operating_activities['GROUP_CFS_OP_ACCOUNTS_PAYABLE'] = {
            'description': _('Accounts Payable'),
            'balance': group_balances['GROUP_CFS_OP_ACCOUNTS_PAYABLE']
        }
        operating_activities['GROUP_CFS_OP_OTHER_CURRENT_ASSETS_ADJUSTMENT'] = {
            'description': _('Other Current Assets'),
            'balance': -group_balances['GROUP_CFS_OP_OTHER_CURRENT_ASSETS_ADJUSTMENT']
        }
        operating_activities['GROUP_CFS_OP_OTHER_CURRENT_LIABILITIES_ADJUSTMENT'] = {
            'description': _('Other Current Liabilities'),
            'balance': group_balances['GROUP_CFS_OP_OTHER_CURRENT_LIABILITIES_ADJUSTMENT']
        }

        net_cash_by_op_activities = sum(i['balance'] for g, i in operating_activities.items())
        self.IO_DIGEST[self.CFS_DIGEST_KEY]['operating'] = operating_activities
        self.IO_DIGEST[self.CFS_DIGEST_KEY]['net_cash_by_activity'] = dict(
            OPERATING=net_cash_by_op_activities
        )

    def financing(self):
        group_balances = self.IO_DIGEST[GroupManager.GROUP_BALANCE_KEY]
        financing_activities = dict()
        financing_activities['GROUP_CFS_FIN_ISSUING_EQUITY'] = {
            'description': _('Common Stock, Preferred Stock and Capital Raised'),
            'balance': sum(a['balance'] for a in self.CASH_ACCOUNTS if a['activity'] == self.JE_MODEL.FINANCING_EQUITY)
        }
        financing_activities['GROUP_CFS_FIN_DIVIDENDS'] = {
            'description': _('Dividends Payed Out to Shareholders'),
            'balance': sum(
                a['balance'] for a in self.CASH_ACCOUNTS if a['activity'] == self.JE_MODEL.FINANCING_DIVIDENDS)
        }
        financing_activities['GROUP_CFS_FIN_ST_DEBT_PAYMENTS'] = {
            'description': _('Increase/Reduction of Short-Term Debt Principal'),
            'balance': sum(a['balance'] for a in self.CASH_ACCOUNTS if a['activity'] == self.JE_MODEL.FINANCING_STD)
        }
        financing_activities['GROUP_CFS_FIN_LT_DEBT_PAYMENTS'] = {
            'description': _('Increase/Reduction of Long-Term Debt Principal'),
            'balance': sum(a['balance'] for a in self.CASH_ACCOUNTS if a['activity'] == self.JE_MODEL.FINANCING_LTD)
        }

        net_cash = sum(i['balance'] for g, i in financing_activities.items())
        self.IO_DIGEST[self.CFS_DIGEST_KEY]['financing'] = financing_activities
        self.IO_DIGEST[self.CFS_DIGEST_KEY]['net_cash_by_activity']['FINANCING'] = net_cash

    def investing(self):
        group_balances = self.IO_DIGEST[GroupManager.GROUP_BALANCE_KEY]
        investing_activities = dict()
        investing_activities['GROUP_CFS_INVESTING_SECURITIES'] = {
            'description': _('Purchase, Maturity and Sales of Investments & Securities'),
            'balance': sum(
                a['balance'] for a in self.CASH_ACCOUNTS if a['activity'] == self.JE_MODEL.INVESTING_SECURITIES)
        }
        investing_activities['GROUP_CFS_INVESTING_PPE'] = {
            'description': _('Addition and Disposition of Property, Plant & Equipment'),
            'balance': sum(
                a['balance'] for a in self.CASH_ACCOUNTS if a['activity'] == self.JE_MODEL.INVESTING_PPE)
        }

        net_cash = sum(i['balance'] for g, i in investing_activities.items())
        self.IO_DIGEST[self.CFS_DIGEST_KEY]['investing'] = investing_activities
        self.IO_DIGEST[self.CFS_DIGEST_KEY]['net_cash_by_activity']['INVESTING'] = net_cash

    def net_cash(self):
        self.IO_DIGEST[self.CFS_DIGEST_KEY]['net_cash'] = sum([
            bal for act, bal in self.IO_DIGEST[self.CFS_DIGEST_KEY]['net_cash_by_activity'].items()
        ])

    def digest(self):
        self.check_io_digest()
        self.operating()
        self.financing()
        self.investing()
        self.net_cash()
        return self.IO_DIGEST
