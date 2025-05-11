#!/usr/bin/env python3
"""Server class with hypermedia pagination for popular baby names dataset."""
import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate start and end indexes for a given page and page size.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indexes.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a dataset of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the Server instance."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset.

        Returns:
            List[List]: The dataset loaded from the CSV file.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page of the dataset.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows from the dataset for the given page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Return a dictionary with pagination info and data.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            Dict[str, Any]: Dictionary with page data and hypermedia info.
        """
        data = self.get_page(page, page_size)
        total = len(self.dataset())
        total_pages = math.ceil(total / page_size)
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }