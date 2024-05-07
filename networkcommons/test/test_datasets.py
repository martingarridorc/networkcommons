from networkcommons.datasets import get_available_datasets, download_dataset, download_url, deseq2_analysis
import pytest
import pandas as pd

# Test get_available_datasets
def test_get_available_datasets():
    # Call the get_available_datasets function
    datasets = get_available_datasets()

    # Assert that the returned value is a list
    assert isinstance(datasets, list)

    # Assert that the returned list is not empty
    assert len(datasets) > 0


def test_download_dataset():
    # Call the download_dataset function with a specific dataset
    dataset = 'panacea'
    data = download_dataset(dataset)

    # Assert that the returned value is a list
    assert isinstance(data, list)

    # Assert that the returned list is not empty
    assert len(data) > 0

def test_deseq2_analysis():
    # Create a dummy dataset for testing, samples as colnames and genes as rownames
    counts = pd.DataFrame({
        'gene_symbol': ['Gene1', 'Gene2', 'Gene3'],
        'Sample1': [90, 150, 10],
        'Sample2': [80, 60, 9],
        'Sample3': [100, 80, 12],
        'Sample4': [100, 120, 17]
    })

    metadata = pd.DataFrame({
        'sample_ID': ['Sample1', 'Sample2', 'Sample3', 'Sample4'],
        'group': ['Control', 'Treatment', 'Treatment', 'Control']
    })

    # Call the deseq2_analysis function
    result = deseq2_analysis(counts, metadata)

    # Assert that the returned value is a pandas DataFrame
    assert isinstance(result, pd.DataFrame)

    # Assert that the DataFrame has the expected columns
    assert 'log2FoldChange' in result.columns
    assert 'lfcSE' in result.columns
    assert 'stat' in result.columns
    assert 'pvalue' in result.columns
    assert 'padj' in result.columns

    # Assert that the DataFrame has the expected content
    data = {
        'baseMean': [93.233027, 101.285704, 11.793541],
        'log2FoldChange': [-0.218172, 0.682183, 0.052954],
        'lfcSE': [0.328036, 0.352393, 0.521659],
        'stat': [-0.665087, 1.935862, 0.101510],
        'pvalue': [0.505995, 0.052885, 0.919146],
        'padj': [0.758992, 0.158654, 0.919146]
    }
    
    expected_result = pd.DataFrame(data, index=['Gene1', 'Gene2', 'Gene3'])
    pd.testing.assert_frame_equal(result, expected_result, check_exact=False)
