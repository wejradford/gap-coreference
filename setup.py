import setuptools

setuptools.setup(
    name='gap-coreference',
    version='0.0.1',
    packages=['gap_coreference'],
    scripts=['gap_coreference/gap_scorer.py'],
    url='https://github.com/google-research-datasets/gap-coreference',
    license='LICENSE',
    description='Packaged version of GAP Coreference scorer.',
    long_description=open('README.md').read(),
)
