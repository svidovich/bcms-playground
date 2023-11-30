import argparse
import csv
import os
import json


# NOTE Don't sort.
tsv_fields = [
    "src_url",
    "trg_url",
    "src_text",
    "trg_text",
    "bleualign_score",
    "src_deferred_hash",
    "trg_deferred_hash",
    "src_paragraph_id",
    "trg_paragraph_id",
    "src_doc_title",
    "trg_doc_title",
    "src_crawl_date",
    "trg_crawl_date",
    "src_file_type",
    "trg_file_type",
    "src_boilerplate",
    "trg_boilerplate",
    "src_heading_html_tag",
    "trg_heading_html_tag",
    "bifixer_hash",
    "bifixer_score",
    "bicleaner_ai_score",
    "biroamer_entities_detected",
    "dsi",
    "translation_direction",
    "en_document_level_variant",
    "domain_en",
    "en_domain_level_variant",
]


def main() -> None:
    parser = argparse.ArgumentParser(description="Parsing MaCoCu datasets.")
    parser.add_argument(
        "-i", "--input-file", required=True, help="Your MaCoCu TSV document."
    )
    parser.add_argument(
        "-n",
        "--count",
        required=False,
        default=1000,
        type=int,
        help="The number of entries for each file.",
    )
    parser.add_argument("-o", "--output-dir", required=False, default="output")

    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    with open(args.input_file) as file_handle:
        next(file_handle)  # Skip the header
        files_written = 0
        eof = True
        while True:
            entry_count = 0
            file_name = f"output_{files_written}.csv"
            current_output_file = open(os.path.join(args.output_dir, file_name), "w")
            writer = csv.DictWriter(current_output_file, fieldnames=tsv_fields)
            for line in file_handle:
                components = line.rstrip().split("\t")
                dictionary = dict(zip(tsv_fields, components))
                if entry_count == 0:
                    writer.writeheader()
                writer.writerow(dictionary)
                entry_count += 1
                if entry_count % args.count == 0:
                    eof = False
                    break
            else:
                eof = True
            print(f"Closing {file_name} after {entry_count} entries.")
            current_output_file.close()
            files_written += 1
            if eof is True:
                print(f"Wrote {files_written} files!")
                break
            entry_count = 0


if __name__ == "__main__":
    main()
