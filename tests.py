# Python ED25519 Bindings
#
# Copyright 2018-2020 Stichting Polkascan (Polkascan Foundation).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

import bip39
import ed25519_dalek


class MyTestCase(unittest.TestCase):
    def test_sign_and_verify_message(self):

        message = b"test"

        # Get private and public key from seed
        seed = bip39.bip39_to_mini_secret('daughter song common combine misery cotton audit morning stuff weasel flee field','')
        private_key, public_key = ed25519_dalek.ed_from_seed(bytes(seed))

        # Generate signature
        signature = ed25519_dalek.ed_sign(public_key, private_key, message)

        # Verify message with signature
        self.assertTrue(ed25519_dalek.ed_verify(signature, message, public_key))

    def test_verify_signature(self):
        # Get private and public key from seed
        seed = bip39.bip39_to_mini_secret(
            'daughter song common combine misery cotton audit morning stuff weasel flee field', '')
        private_key, public_key = ed25519_dalek.ed_from_seed(bytes(seed))

        signature = bytes.fromhex("6168a361ec4d5f0bc78d2f1db1ea59b1516baf149e75d1a9b9732b16834c6f71"
                                  "843dec967c6399c570ae014fd44a06ca4332f7bf562faf9134a20d169380a003")

        # Verify message with signature
        self.assertFalse(ed25519_dalek.ed_verify(signature, b"test", public_key))

    def test_verify_invalid_signature(self):
        # Get private and public key from seed
        seed = bip39.bip39_to_mini_secret(
            'daughter song common combine misery cotton audit morning stuff weasel flee field', '')
        private_key, public_key = ed25519_dalek.ed_from_seed(bytes(seed))

        # Verify message with signature
        self.assertFalse(ed25519_dalek.ed_verify(bytes(32), b"test", public_key))

    def test_invalid_seed_length(self):
        self.assertRaises(ValueError, ed25519_dalek.ed_from_seed, bytes(1))

    def test_sign_invalid_pub_key_length(self):
        # Get private and public key from seed
        seed = bip39.bip39_to_mini_secret(
            'daughter song common combine misery cotton audit morning stuff weasel flee field', '')
        private_key, _ = ed25519_dalek.ed_from_seed(bytes(seed))

        self.assertRaises(ValueError, ed25519_dalek.ed_sign, bytes(1), private_key, b"test")


if __name__ == '__main__':
    unittest.main()
