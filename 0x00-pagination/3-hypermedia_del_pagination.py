#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination."""
import csv
from typing import List, Dict, Any


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of start and end indexes for pagination."""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"


    def __init__(self) -> None:
        """
        Initialize the Server with dataset and
        indexed dataset set to None.
        """
        self.__dataset = None
        self.__indexed_dataset = None


    def dataset(self) -> List[List]:
        """Cached dataset loaded from CSV file, skipping the header row."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset


    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset


    def get_hyper_index(
            self, index: int = None, page_size: int = 10
            ) -> Dict[str, Any]:
        """Return deletion-resilient hypermedia pagination info
        starting from index.

        Args:
            index (int): The current start index of the return page.
            page_size (int): The current page size.

        Returns:
            Dict[str, Any]:
            Dictionary with index, next_index, page_size, and data.
        """
        assert isinstance(index, int) and index >= 0
        indexed = self.indexed_dataset()
        assert index < len(indexed)
        data = []
        current = index
        count = 0
        while count < page_size and current < len(self.dataset()):
            if current in indexed:
                data.append(indexed[current])
                count += 1
            current += 1
        return {
            'index': index,
            'next_index': current,
            'page_size': len(data),
            'data': data
        }
