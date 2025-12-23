from dataclasses import dataclass, field
from typing import Iterator
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

DATA_TXT = Path(__file__).parent / "data.txt"

@dataclass
class Present:
    id: int
    size: int
    pattern: str

@dataclass
class Region:
    area: int
    grid: list[list[int]] = field(default_factory=list)
    presents: list[int] = field(default_factory=list)

def open_data_file() -> str:
    with DATA_TXT.open("r", encoding="utf-8") as file:
        return file.read()

def divide_data(data: str) -> Iterator[str]:
    for line in data.split("\n\n"):
        yield line

def load_presents(presents: list[str]) -> Iterator[Present]:
    for item in presents:
        parts = item.split(":\n")
        yield Present(id=int(parts[0]), size=parts[1].count("#"), pattern=parts[1])

def load_regions(regions: str) -> Iterator[Region]:
    for line in regions.split("\n"):
        parts = line.split(":")
        x, y = map(int, parts[0].strip().split("x"))
        grid = [[0 for _ in range(x)] for _ in range(y)]
        presents = list(map(int, parts[1].strip().split()))
        yield Region(area=x * y, grid=grid, presents=presents)

def validate_region_by_max_area(region: Region, presents: list[Present]) -> bool:
    total_size = sum(p.size * region.presents[p.id] for p in presents)
    return total_size <= region.area

def validate_region_by_blocks(region: Region, presents: list[Present]) -> bool:
    blocks = sum(9 * region.presents[p.id] for p in presents)
    return blocks <= region.area

def main() -> None:
    data = list(divide_data(open_data_file()))
    logging.info(f"Data loaded: {data[:2]}... {data[-1][:20]}...")
    presents = list(load_presents(data[:-1]))
    regions = list(load_regions(data[-1]))
    logging.info(f"Presents loaded: {presents[:2]}... Total: {len(presents)}")
    logging.info(f"Regions loaded: {str(regions[:1])[:50]}... Total: {len(regions)}")

    print("Valid regions by max_area: ", sum(1 for region in regions if validate_region_by_max_area(region, presents)))
    print("Valid regions by blocks: ", sum(1 for region in regions if validate_region_by_blocks(region, presents)))
    # The max_area checks if the total size of presents fits in the region area.
    # Meaning all that fails this test can't fit into the region at all.
    # 
    # The blocks checks if the 3x3 area that each present "occupies" fits into the region space.
    # Meaning that all that if it passes this test, it is guaranteed to fit into the region.
    #
    # Since both tests reslult in the same count for the provided data, we know that all regions that can in a best case scenario fit the presents, also can fit them by blocks.
    # In other words, we don't have to try to rotate and find space for the presents as there is enough space for them all to fit.


if __name__ == "__main__":
    main()