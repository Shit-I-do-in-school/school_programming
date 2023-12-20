for platform in map:
    next_platform = f"omr{int(platform[-1:]) + 1}"
    travel_path = f"{platform}-omr{int(platform[-1:]) + 1}"
    paths = map[platform]

    if next_platform in paths:
        min_trav[travel_path] = paths[next_platform]

    else:
        for av_platform in map[platform]:
            if next_platform in map[av_platform]:
                min_trav[travel_path] = paths[av_platform] + map[av_platform][next_platform]

            else:
                for av2_platform in map[av_platform]:
                    if next_platform in map[av2_platform]:
                        travel_cost = paths[av_platform] + map[av2_platform][next_platform] + map[av_platform][av2_platform]

                        #calculate final cost and steps
                        if travel_path in min_trav:
                            if travel_cost < min_trav[travel_path]:
                                min_trav[travel_path] = travel_cost
                        else:
                            min_trav[travel_path] = travel_cost