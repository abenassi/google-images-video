from setuptools import setup

setup(name='google_images_video',
      version='0.1.0',
      description='Make videos with google images',
      url='https://github.com/abenassi/google_images_video',
      author='Agustin Benassi',
      author_email='agusbenassi@gmail.com',
      license='MIT',

      packages=['gimvideo'],

      test_suite='nose.collector',
      tests_require=['nose', 'nose-cov']
      )