.class Lcom/android/calculator2/Calculator$PageAdapter;
.super Landroid/support/v4/view/PagerAdapter;
.source "Calculator.java"


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/calculator2/Calculator;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = "PageAdapter"
.end annotation


# instance fields
.field private mAdvancedPage:Landroid/view/View;

.field private mSimplePage:Landroid/view/View;

.field final synthetic this$0:Lcom/android/calculator2/Calculator;


# direct methods
.method public constructor <init>(Lcom/android/calculator2/Calculator;Landroid/support/v4/view/ViewPager;)V
    .locals 11
    .parameter
    .parameter "parent"

    .prologue
    const/4 v10, 0x0

    .line 265
    iput-object p1, p0, Lcom/android/calculator2/Calculator$PageAdapter;->this$0:Lcom/android/calculator2/Calculator;

    invoke-direct {p0}, Landroid/support/v4/view/PagerAdapter;-><init>()V

    .line 266
    invoke-virtual {p2}, Landroid/support/v4/view/ViewPager;->getContext()Landroid/content/Context;

    move-result-object v9

    invoke-static {v9}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;

    move-result-object v5

    .line 267
    .local v5, inflater:Landroid/view/LayoutInflater;
    const v9, 0x7f040003

    invoke-virtual {v5, v9, p2, v10}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;Z)Landroid/view/View;

    move-result-object v8

    .line 268
    .local v8, simplePage:Landroid/view/View;
    const/high16 v9, 0x7f04

    invoke-virtual {v5, v9, p2, v10}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;Z)Landroid/view/View;

    move-result-object v1

    .line 269
    .local v1, advancedPage:Landroid/view/View;
    iput-object v8, p0, Lcom/android/calculator2/Calculator$PageAdapter;->mSimplePage:Landroid/view/View;

    .line 270
    iput-object v1, p0, Lcom/android/calculator2/Calculator$PageAdapter;->mAdvancedPage:Landroid/view/View;

    .line 272
    invoke-virtual {p1}, Lcom/android/calculator2/Calculator;->getResources()Landroid/content/res/Resources;

    move-result-object v6

    .line 273
    .local v6, res:Landroid/content/res/Resources;
    const/high16 v9, 0x7f05

    invoke-virtual {v6, v9}, Landroid/content/res/Resources;->obtainTypedArray(I)Landroid/content/res/TypedArray;

    move-result-object v7

    .line 274
    .local v7, simpleButtons:Landroid/content/res/TypedArray;
    const/4 v4, 0x0

    .local v4, i:I
    :goto_0
    invoke-virtual {v7}, Landroid/content/res/TypedArray;->length()I

    move-result v9

    if-ge v4, v9, :cond_0

    .line 275
    invoke-virtual {v7, v4, v10}, Landroid/content/res/TypedArray;->getResourceId(II)I

    move-result v9

    invoke-virtual {p1, v8, v9}, Lcom/android/calculator2/Calculator;->setOnClickListener(Landroid/view/View;I)V

    .line 274
    add-int/lit8 v4, v4, 0x1

    goto :goto_0

    .line 277
    :cond_0
    invoke-virtual {v7}, Landroid/content/res/TypedArray;->recycle()V

    .line 279
    const v9, 0x7f050001

    invoke-virtual {v6, v9}, Landroid/content/res/Resources;->obtainTypedArray(I)Landroid/content/res/TypedArray;

    move-result-object v0

    .line 280
    .local v0, advancedButtons:Landroid/content/res/TypedArray;
    const/4 v4, 0x0

    :goto_1
    invoke-virtual {v0}, Landroid/content/res/TypedArray;->length()I

    move-result v9

    if-ge v4, v9, :cond_1

    .line 281
    invoke-virtual {v0, v4, v10}, Landroid/content/res/TypedArray;->getResourceId(II)I

    move-result v9

    invoke-virtual {p1, v1, v9}, Lcom/android/calculator2/Calculator;->setOnClickListener(Landroid/view/View;I)V

    .line 280
    add-int/lit8 v4, v4, 0x1

    goto :goto_1

    .line 283
    :cond_1
    invoke-virtual {v0}, Landroid/content/res/TypedArray;->recycle()V

    .line 285
    const v9, 0x7f0c0011

    invoke-virtual {v8, v9}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v3

    .line 286
    .local v3, clearButton:Landroid/view/View;
    if-eqz v3, :cond_2

    .line 287
    #setter for: Lcom/android/calculator2/Calculator;->mClearButton:Landroid/view/View;
    invoke-static {p1, v3}, Lcom/android/calculator2/Calculator;->access$002(Lcom/android/calculator2/Calculator;Landroid/view/View;)Landroid/view/View;

    .line 290
    :cond_2
    const v9, 0x7f0c0012

    invoke-virtual {v8, v9}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v2

    .line 291
    .local v2, backspaceButton:Landroid/view/View;
    if-eqz v2, :cond_3

    .line 292
    #setter for: Lcom/android/calculator2/Calculator;->mBackspaceButton:Landroid/view/View;
    invoke-static {p1, v2}, Lcom/android/calculator2/Calculator;->access$102(Lcom/android/calculator2/Calculator;Landroid/view/View;)Landroid/view/View;

    .line 294
    :cond_3
    return-void
.end method


# virtual methods
.method public destroyItem(Landroid/view/View;ILjava/lang/Object;)V
    .locals 0
    .parameter "container"
    .parameter "position"
    .parameter "object"

    .prologue
    .line 314
    check-cast p1, Landroid/view/ViewGroup;

    .end local p1
    check-cast p3, Landroid/view/View;

    .end local p3
    invoke-virtual {p1, p3}, Landroid/view/ViewGroup;->removeView(Landroid/view/View;)V

    .line 315
    return-void
.end method

.method public finishUpdate(Landroid/view/View;)V
    .locals 0
    .parameter "container"

    .prologue
    .line 319
    return-void
.end method

.method public getCount()I
    .locals 1

    .prologue
    .line 298
    const/4 v0, 0x2

    return v0
.end method

.method public instantiateItem(Landroid/view/View;I)Ljava/lang/Object;
    .locals 1
    .parameter "container"
    .parameter "position"

    .prologue
    .line 307
    if-nez p2, :cond_0

    iget-object v0, p0, Lcom/android/calculator2/Calculator$PageAdapter;->mSimplePage:Landroid/view/View;

    .line 308
    .local v0, page:Landroid/view/View;
    :goto_0
    check-cast p1, Landroid/view/ViewGroup;

    .end local p1
    invoke-virtual {p1, v0}, Landroid/view/ViewGroup;->addView(Landroid/view/View;)V

    .line 309
    return-object v0

    .line 307
    .end local v0           #page:Landroid/view/View;
    .restart local p1
    :cond_0
    iget-object v0, p0, Lcom/android/calculator2/Calculator$PageAdapter;->mAdvancedPage:Landroid/view/View;

    goto :goto_0
.end method

.method public isViewFromObject(Landroid/view/View;Ljava/lang/Object;)Z
    .locals 1
    .parameter "view"
    .parameter "object"

    .prologue
    .line 323
    if-ne p1, p2, :cond_0

    const/4 v0, 0x1

    :goto_0
    return v0

    :cond_0
    const/4 v0, 0x0

    goto :goto_0
.end method

.method public restoreState(Landroid/os/Parcelable;Ljava/lang/ClassLoader;)V
    .locals 0
    .parameter "state"
    .parameter "loader"

    .prologue
    .line 333
    return-void
.end method

.method public saveState()Landroid/os/Parcelable;
    .locals 1

    .prologue
    .line 328
    const/4 v0, 0x0

    return-object v0
.end method

.method public startUpdate(Landroid/view/View;)V
    .locals 0
    .parameter "container"

    .prologue
    .line 303
    return-void
.end method
