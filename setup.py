from setuptools import setup, find_packages

setup(
    name="myapp",
    version="1.0.0",
    author="cc",
    author_email="1533181183@163.com",
    description="test setup",
    # 项目主页
    url="https://google.com/",

    # 你要安装的包，通过 setuptools.find_packages 找到当前目录下有哪些包
    packages=find_packages(),
    classifiers=[
        # 目标 Python 版本
        'Programming Language :: Python :: 2',
    ],

    # 打包管理
    # 安装过程中，需要安装的静态文件，如配置文件、service文件、图片等
    data_files=[
        ('', ['conf/*.conf']),
        ('/usr/lib/systemd/system/', ['bin/*.service']),
    ],

    # 希望被打包的文件
    package_data={
        '': ['*.md'],
        'bandwidth_reporter': ['*.txt']
    },
    # 不打包某些文件
    exclude_package_data={
        'bandwidth_reporter': ['*.txt']
    },

    # 依赖管理
    # 表明当前模块依赖哪些包，若环境中没有，则会从pypi中下载安装
    install_requires=["docutils>=0.3",
                      "beautifulsoup4==4.11.1",
                      "lxml==4.9.1",
                      "numpy==1.23.1",
                      ],

    # setup.py 本身要依赖的包，这通常是为一些setuptools的插件准备的配置
    # 这里列出的包，不会自动安装。
    setup_requires=['pbr'],

    # 仅在测试时需要使用的依赖，在正常发布的代码中是没有用的。
    # 在执行python setup.py test时，可以自动安装这三个库，确保测试的正常运行。
    tests_require=[
        'pytest>=3.3.1',
        'pytest-cov>=2.5.1',
    ],

    # 用于安装setup_requires或tests_require里的软件包
    # 这些信息会写入egg的 metadata 信息中
    dependency_links=[
        "https://example2.com/p/foobar-1.0.tar.gz",
    ],

    # install_requires 在安装模块时会自动安装依赖包
    # 而 extras_require 不会，这里仅表示该模块会依赖这些包
    # 但是这些包通常不会使用到，只有当你深度使用模块时，才会用到，这里需要你手动安装
    extras_require={
        'PDF': ["ReportLab>=1.2", "RXP"],
        'reST': ["docutils>=0.3"],
    }
)
