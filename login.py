import base64

from Crypto.Cipher import AES


class Login:
    def __init__(self, *args):
        self.username = args[0]
        self.password = args[1]
        self.block_size = 16
        self.AES_KEY = "u2oh6Vu^HWe4_AES"
    def login(self):
        pass

    def pad(self, text):
        """ 对需要加密的明文进行填充补位
        @param text: 需要进行填充补位操作的明文
        @return: 补齐明文字符串
        """
        text_length = len(text)
        # 计算需要填充的位数
        amount_to_pad = self.block_size - (text_length % self.block_size)
        if amount_to_pad == 0:
            amount_to_pad = self.block_size
        # 获得补位所用的字符
        pad = chr(amount_to_pad).encode()
        return text + pad * amount_to_pad

    def encrypt(self, text):
        ciper = AES.new(self.AES_KEY.encode(), AES.MODE_CBC, self.AES_KEY.encode())
        # print(base64.b64encode(ciper.encrypt(self.pad(text.encode()))).decode())
        return base64.b64encode(ciper.encrypt(self.pad(text.encode()))).decode()
    def get_information(self):
        self.username = self.encrypt(self.username)
        self.password = self.encrypt(self.password)
