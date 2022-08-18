from pyteal import Mode
from algopytest import compile_program
from pytest import fixture
from algosdk.future.transaction import LogicSigAccount

# Load the smart signatures from this project. The path to find these
# imports is set by the environment variable `$PYTHONPATH`.
from recurring_payments_smart_sig import recurring_txns


@fixture
def smart_signature(owner, user1):
    compiled_program = compile_program(recurring_txns(user1.address), mode=Mode.Signature)
    lsig = LogicSigAccount(compiled_program)
    lsig.sign(owner.private_key)
    return lsig
