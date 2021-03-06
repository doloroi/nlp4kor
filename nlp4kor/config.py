import logging
import os
import sys

from bage_utils.base_util import db_hostname, is_my_pc, is_my_gpu_pc
from bage_utils.log_util import LogUtil

# warnings.simplefilter(action='ignore', category=FutureWarning)

log = None
if log is None:
    if is_my_pc():  # my pc(pycharm client, mac)
        log = LogUtil.get_logger(None, level=logging.DEBUG, console_mode=True)  # global log
    if is_my_gpu_pc():  # gpu pc(pycharm remote, ubuntu)
        if len(sys.argv) == 1: # remote mode
            log = LogUtil.get_logger(None, level=logging.INFO, console_mode=True)  # global log
        else: # batch mode
            log = LogUtil.get_logger(sys.argv[0], level=logging.INFO, console_mode=False)  # global log
    else:  # gpu pc(batch job, ubuntu)
        log = LogUtil.get_logger(sys.argv[0], level=logging.INFO, console_mode=False)  # global log # console_mode=True for jupyter notebook

MONGO_URL = r'mongodb://%s:%s@%s:%s/%s?authMechanism=MONGODB-CR' % (
    'root', os.getenv('MONGODB_PASSWD'), 'db-local', '27017', 'admin')
MYSQL_URL = {'host': db_hostname(), 'user': 'root', 'passwd': os.getenv('MYSQL_PASSWD'), 'db': 'kr_nlp'}

PROJECT_DIR = os.path.join(os.getenv("HOME"), 'workspace/nlp4kor')
# log.info('PROJECT_DIR: %s' % PROJECT_DIR)

DATA_DIR = os.path.join(PROJECT_DIR, 'data/')
# log.info('DATA_DIR: %s' % DATA_DIR)
if not os.path.exists(DATA_DIR):
    os.mkdir(DATA_DIR)

TENSORBOARD_LOG_DIR = os.path.join(os.getenv("HOME"), 'tensorboard_log')
# log.info('TENSORBOARD_LOG_DIR: %s' % TENSORBOARD_LOG_DIR)
if not os.path.exists(TENSORBOARD_LOG_DIR):
    os.mkdir(TENSORBOARD_LOG_DIR)

# dataset repositories
MNIST_DIR = os.path.join(os.getenv('HOME'), 'workspace', 'nlp4kor-mnist')
MNIST_DATA_DIR = os.path.join(MNIST_DIR, 'data')
MNIST_CNN_MODEL_DIR = os.path.join(MNIST_DIR, 'models', 'cnn')
MNIST_DAE_MODEL_DIR = os.path.join(MNIST_DIR, 'models', 'dae')

KO_WIKIPEDIA_ORG_DIR = os.path.join(os.getenv('HOME'), 'workspace', 'nlp4kor-ko.wikipedia.org')

KO_WIKIPEDIA_ORG_INFO_FILE = os.path.join(KO_WIKIPEDIA_ORG_DIR, 'data', 'ko.wikipedia.org.info.txt')
KO_WIKIPEDIA_ORG_URLS_FILE = os.path.join(KO_WIKIPEDIA_ORG_DIR, 'data', 'ko.wikipedia.org.urls.txt')
KO_WIKIPEDIA_ORG_CHARACTERS_FILE = os.path.join(KO_WIKIPEDIA_ORG_DIR, 'dic', 'ko.wikipedia.org.characters')

KO_WIKIPEDIA_ORG_SENTENCES_FILE = os.path.join(KO_WIKIPEDIA_ORG_DIR, 'data', 'ko.wikipedia.org.sentences.gz')
KO_WIKIPEDIA_ORG_TRAIN_SENTENCES_FILE = os.path.join(KO_WIKIPEDIA_ORG_DIR, 'data', 'ko.wikipedia.org.train.sentences.gz')
KO_WIKIPEDIA_ORG_VALID_SENTENCES_FILE = os.path.join(KO_WIKIPEDIA_ORG_DIR, 'data', 'ko.wikipedia.org.valid.sentences.gz')
KO_WIKIPEDIA_ORG_TEST_SENTENCES_FILE = os.path.join(KO_WIKIPEDIA_ORG_DIR, 'data', 'ko.wikipedia.org.test.sentences.gz')

KO_WIKIPEDIA_ORG_WORD_SPACING_MODEL_DIR = os.path.join(KO_WIKIPEDIA_ORG_DIR, 'models', 'word_spacing')
KO_WIKIPEDIA_ORG_SPELLING_ERROR_CORRECTION_MODEL_DIR = os.path.join(KO_WIKIPEDIA_ORG_DIR, 'models', 'spelling_error_correction')

if __name__ == '__main__':
    print('DATA_DIR:', MNIST_DIR)
    print('MONGODB_PASSWD', os.getenv('MONGODB_PASSWD'), os.environ.get('MONGODB_PASSWD'))
