const $app = $('#app');
const compare = (data1, data2) => {

    let diff = 0;
    for (let i = 0; i < data1.length; i++) {
        if (data1[i] !== data2[i]) {
            diff += 1;
        }
    }
    return diff;
};
data.forEach(item => item.diffs = []);
data.forEach(item => {
    data.forEach(item2 => {
        if (item.image !== item2.image) {
            const diff = compare(item.sign_data, item2.sign_data);
            item.diffs.push([item2.image, diff]);
            // item2.diffs.push([item.image, diff]);
        }
    });
});
data.forEach(item => item.diffs.sort(([_, d], [__, d2]) => d - d2));
const showTable = json => {
    const $table = $('<table>');
    json.forEach((data) => {
        const {image, sign, diffs} = data;
        const $tr = $(`<tr>
                <td><img src="${image}" width="100"></td>
                <td><img src="${sign}" width="100"></td>
            </tr>`);
        for (const [image, diff] of diffs) {
            $tr.append($(`
                <td>${diff}: <img src="${image}" width="100"></td>
            `))
        }
        $table.append($tr);
    });
    $app.empty().append($table);
};



showTable(data);