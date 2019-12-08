try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : '테스트 프로젝트',
    'author' : 'qqplot',
    'url' : 'https://github.com/qqplot/SideProject01',
    'download_url' : 'https://github.com/qqplot/SideProject01.git',
    'author_email' : 'kyubyung91@gmail.com',
    'version' : '0.1',
    'install_requires' : ['pytest'],
    'packages' : ['ex47'],
    'scripts' : [],
    'name' : 'test project', # 한글을 쓸 수 없습니다.
}

setup(**config)
