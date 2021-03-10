from string import punctuation
from collections import Counter



def create_clean_list(text):
    text = text.split()
    new_text = []
    for t in text:
        element = t.strip("?").strip("'").strip("!").strip("/")
        for i in punctuation:
            if i not in element or i == "'":
                continue
            elif len(set(list(element))) < 2:
                continue
            else:
                for e in element.split(i):
                    new_text.append(e.lower())
                element = ""
        if element:
            new_text.append(element.lower())
    return new_text


def top_3_words(text):
    words = create_clean_list(text)
    word_counts = Counter(words)
    top_10 = word_counts.most_common(10)
    print(top_10)
    return [t[0] for t in top_10 if t[0].isalpha() or "'" in t[0]]


print("max occurencies: a/ cd't '' D?d d! e// --- ", top_3_words("a/ cd't '' D?d d! e//"))
print("max occurencies:   ...  ", top_3_words("gUeI!qrfObIjmH!,zcOv kFoIDx;/fZEJQEjARf?-kFoIDx??'RdyZpAs;LLaJwF'HzI? ;:DcdxTFqftp;::??qewbOz_:.LswGoofjd,qewbOz?__ zcOv:qrfObIjmH?fZEJQEjARf../mPWyQef-LLaJwF'HzI-;/,EONNhDRSPg !LswGoofjd .;?-'RdyZpAs.;?/qewbOz!;.?!xPmUBcht-.;.zcOv--/DcdxTFqftp_/_-/qrfObIjmH  .! DcdxTFqftp/_ zcOv:noGDFQQsTx/;/-;xPmUBcht,!!?/fZEJQEjARf.-;-:qewbOz,;;/noGDFQQsTx_ :fZEJQEjARf!,?_'RdyZpAs,:?;mPWyQef_noGDFQQsTx !fZEJQEjARf//ZlsuH;-DcdxTFqftp;,- !zcOv? qrfObIjmH _zcOv-?qewbOz--._:qewbOz,._,EONNhDRSPg?-,/ qewbOz /:!zcOv:LLaJwF'HzI,?: LLaJwF'HzI;!/qrfObIjmH,.,.ZlsuH,.kFoIDx./_/kFoIDx! .qrfObIjmH__,;LswGoofjd_-/?;zcOv/?kFoIDx;;:!zcOv  _!ZlsuH- !:!LswGoofjd:/? 'RdyZpAs,-_;!noGDFQQsTx-/ yb'nzR/-/_'RdyZpAs_/,_ qewbOz_DcdxTFqftp_?'RdyZpAs :_ _yb'nzR._?:noGDFQQsTx _,_:mPWyQef.IRfXArB;/!!'RdyZpAs?: !-fZEJQEjARf,.??!IRfXArB-qrfObIjmH__;kFoIDx -DcdxTFqftp:noGDFQQsTx // IRfXArB!:;! noGDFQQsTx:_?LLaJwF'HzI;!?_EONNhDRSPg;noGDFQQsTx!.!!_qewbOz.zcOv!,!_;kFoIDx;_-DcdxTFqftp-qrfObIjmH?ZlsuH,_?:kFoIDx/qrfObIjmH, xPmUBcht ?-kFoIDx-?,!!mPWyQef-!.IRfXArB-,; xPmUBcht /fZEJQEjARf!.:--EONNhDRSPg/ zcOv;kFoIDx:xPmUBcht:.!!/LLaJwF'HzI,;!,fZEJQEjARf!,!EONNhDRSPg_zcOv_/ _;kFoIDx;qewbOz ,!.DcdxTFqftp,;?.mPWyQef-_/,_'RdyZpAs. xPmUBcht.kFoIDx.;; qewbOz!---;LswGoofjd_!?.LswGoofjd!zcOv.EONNhDRSPg,!:_'RdyZpAs:,.DcdxTFqftp:/!;,kFoIDx!;:-?noGDFQQsTx:noGDFQQsTx,zcOv.LLaJwF'HzI,--:uCPGgfVh/!.,mPWyQef,!-EONNhDRSPg/ kFoIDx!ZlsuH//zcOv!;. -noGDFQQsTx__noGDFQQsTx-/-_LLaJwF'HzI,;-, qrfObIjmH!,.-qewbOz?-:.kFoIDx;:.?gUeI_;? fZEJQEjARf?;fZEJQEjARf?. _kFoIDx!?!;-zcOv/?'RdyZpAs_--?qewbOz! -,mPWyQef  ,kFoIDx.!!.,LswGoofjd._?DcdxTFqftp ,/;/qewbOz.:qewbOz:?mPWyQef_IRfXArB?/-LLaJwF'HzI/;?xPmUBcht?LswGoofjd_xPmUBcht ?mPWyQef-!-LLaJwF'HzI/:LLaJwF'HzI,: ._qewbOz: .'RdyZpAs. ,;zcOv::IRfXArB:-qrfObIjmH-.mPWyQef!'RdyZpAs:? fZEJQEjARf_LswGoofjd !_ ydOX'_?_kFoIDx,- LLaJwF'HzI.!kFoIDx ,.:!noGDFQQsTx;,!?EONNhDRSPg.??--mPWyQef;.?qrfObIjmH:qewbOz/uCPGgfVh?.!_!EONNhDRSPg: DcdxTFqftp ,LswGoofjd_,!:;LLaJwF'HzI!:.qewbOz-!_;;xPmUBcht,.::?qrfObIjmH;.noGDFQQsTx?,: zcOv!LswGoofjd_,?.,IRfXArB:mPWyQef?LswGoofjd !!gUeI?!!:mPWyQef DcdxTFqftp-?/IRfXArB:?EONNhDRSPg_gUeI/-fZEJQEjARf,ZlsuH/zcOv-?/_LLaJwF'HzI/LLaJwF'HzI-:.!LswGoofjd_xPmUBcht,/-ZlsuH;:IRfXArB;?!_noGDFQQsTx ,?/EONNhDRSPg/ _?:kFoIDx?_  qewbOz;:!uCPGgfVh:uCPGgfVh_, :?DcdxTFqftp! zcOv._,kFoIDx/!:EONNhDRSPg zcOv.--?LswGoofjd/,/!;uCPGgfVh?/__.yb'nzR!fZEJQEjARf kFoIDx/,!; zcOv!.?,!EONNhDRSPg,. _LLaJwF'HzI-: -LLaJwF'HzI ;?: DcdxTFqftp-!.,?mPWyQef-_.xPmUBcht.,!:_zcOv.,-qewbOz,_,,.kFoIDx?mPWyQef//,_;kFoIDx -; ?LswGoofjd:_:,fZEJQEjARf., LswGoofjd.-fZEJQEjARf!.:;/LLaJwF'HzI;:./qrfObIjmH.-;:;LLaJwF'HzI-;:noGDFQQsTx:mPWyQef_-_/;qewbOz:?;?!noGDFQQsTx;xPmUBcht,yb'nzR EONNhDRSPg-??ZlsuH/-?:!IRfXArB!/;!;'RdyZpAs .? !LLaJwF'HzI.::!kFoIDx:._;:fZEJQEjARf;-LLaJwF'HzI ;;.IRfXArB?DcdxTFqftp!;!fZEJQEjARf!;,;/qrfObIjmH_-kFoIDx/.,_noGDFQQsTx?'RdyZpAs/_noGDFQQsTx;;LLaJwF'HzI! ? ;qrfObIjmH:!?noGDFQQsTx!;LswGoofjd! ;,/zcOv_'RdyZpAs,-:!'RdyZpAs - DcdxTFqftp_?:!;noGDFQQsTx !?!?mPWyQef;:;mPWyQef:/?kFoIDx? ..zcOv.//!:DcdxTFqftp: !LLaJwF'HzI??;LswGoofjd?  -mPWyQef_:.!_uCPGgfVh!! /xPmUBcht..;_:uCPGgfVh/?,;zcOv !LLaJwF'HzI,EONNhDRSPg /_?DcdxTFqftp?/kFoIDx.:. ?fZEJQEjARf.,  zcOv yb'nzR;_!,LswGoofjd_-.;."))
print("max occurencies:   '''  ", top_3_words("  '''  "))
# print("max occurencies: ", top_3_words(""))
# print(list("khvkjv -"))



